#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import pathlib
import sys
import urllib.parse
import urllib.request


BASE = "https://picsum.photos"


def _positive_int(value: str) -> int:
    try:
        n = int(value)
    except ValueError as e:
        raise argparse.ArgumentTypeError("must be an integer") from e
    if n <= 0:
        raise argparse.ArgumentTypeError("must be > 0")
    return n


def _blur_int(value: str) -> int:
    n = _positive_int(value)
    if n < 1 or n > 10:
        raise argparse.ArgumentTypeError("blur must be 1..10")
    return n


def _build_url(
    *,
    width: int | None,
    height: int | None,
    size: int | None,
    image_id: str | None,
    seed: str | None,
    grayscale: bool,
    blur: int | None,
    random: str | None,
    ext: str | None,
) -> str:
    if size is not None and (width is not None or height is not None):
        raise SystemExit("error: use either --size OR --width/--height")
    if (width is None) ^ (height is None):
        raise SystemExit("error: --width and --height must be used together")
    if size is None and width is None:
        raise SystemExit("error: provide --size OR --width/--height")
    if seed and image_id:
        raise SystemExit("error: use either --seed OR --id (not both)")

    path_parts: list[str] = []
    if seed:
        path_parts += ["seed", seed]
    if image_id:
        path_parts += ["id", str(image_id)]

    if size is not None:
        path_parts += [str(size)]
    else:
        path_parts += [str(width), str(height)]

    path = "/".join(path_parts)
    if ext:
        ext = ext.lstrip(".").lower()
        if ext not in {"jpg", "jpeg", "webp", "png"}:
            raise SystemExit("error: --ext must be one of jpg, jpeg, png, webp")
        path = f"{path}.{ext}"

    url = f"{BASE}/{path}"

    qs: dict[str, str | None] = {}
    if grayscale:
        qs["grayscale"] = None
    if blur is not None:
        qs["blur"] = str(blur)
    if random is not None:
        qs["random"] = str(random)

    if qs:
        # Keep valueless params like "?grayscale" (not "?grayscale=")
        parts: list[str] = []
        for k, v in qs.items():
            if v is None:
                parts.append(urllib.parse.quote_plus(k))
            else:
                parts.append(f"{urllib.parse.quote_plus(k)}={urllib.parse.quote_plus(v)}")
        url = f"{url}?{'&'.join(parts)}"

    return url


def cmd_url(args: argparse.Namespace) -> int:
    url = _build_url(
        width=args.width,
        height=args.height,
        size=args.size,
        image_id=args.id,
        seed=args.seed,
        grayscale=args.grayscale,
        blur=args.blur,
        random=args.random,
        ext=args.ext,
    )
    print(url)
    return 0


def _ensure_parent(path: pathlib.Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def cmd_download(args: argparse.Namespace) -> int:
    url = _build_url(
        width=args.width,
        height=args.height,
        size=args.size,
        image_id=args.id,
        seed=args.seed,
        grayscale=args.grayscale,
        blur=args.blur,
        random=args.random,
        ext=args.ext,
    )

    out = pathlib.Path(args.out)
    if out.is_dir() or str(args.out).endswith(("/", "\\")):
        raise SystemExit("error: --out must be a file path (not a directory)")

    _ensure_parent(out)

    req = urllib.request.Request(url, headers={"User-Agent": "random-image-placeholder/1.0"})
    with urllib.request.urlopen(req) as resp:
        data = resp.read()
        final_url = resp.geturl()
        ctype = resp.headers.get("Content-Type", "")

    out.write_bytes(data)

    meta = {
        "requested_url": url,
        "final_url": final_url,
        "content_type": ctype,
        "bytes": len(data),
        "saved_to": os.fspath(out),
    }
    print(json.dumps(meta, ensure_ascii=False, indent=2))
    return 0


def _fetch_json(url: str) -> object:
    req = urllib.request.Request(url, headers={"User-Agent": "random-image-placeholder/1.0"})
    with urllib.request.urlopen(req) as resp:
        data = resp.read()
    return json.loads(data.decode("utf-8"))


def cmd_info(args: argparse.Namespace) -> int:
    if bool(args.id) == bool(args.seed):
        raise SystemExit("error: provide exactly one of --id or --seed")
    if args.id:
        url = f"{BASE}/id/{args.id}/info"
    else:
        url = f"{BASE}/seed/{args.seed}/info"
    obj = _fetch_json(url)
    print(json.dumps(obj, ensure_ascii=False, indent=2))
    return 0


def cmd_list(args: argparse.Namespace) -> int:
    url = f"{BASE}/v2/list?page={args.page}&limit={args.limit}"
    obj = _fetch_json(url)
    print(json.dumps(obj, ensure_ascii=False, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="picsum.py",
        description="Generate Picsum placeholder URLs and optionally download images.",
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    def add_common(sp: argparse.ArgumentParser) -> None:
        size_group = sp.add_argument_group("Size")
        size_group.add_argument("--size", type=_positive_int, help="Square size (e.g. 200)")
        size_group.add_argument("--width", type=_positive_int, help="Width (use with --height)")
        size_group.add_argument("--height", type=_positive_int, help="Height (use with --width)")

        sel = sp.add_argument_group("Selection")
        sel.add_argument("--seed", type=str, help="Stable random seed (e.g. 'avatar-42')")
        sel.add_argument("--id", type=str, help="Specific image id")

        opt = sp.add_argument_group("Options")
        opt.add_argument("--grayscale", action="store_true", help="Add grayscale option")
        opt.add_argument("--blur", type=_blur_int, help="Add blur option (1..10)")
        opt.add_argument("--random", type=str, help="Cache-busting param value (e.g. 1, 2, ...)")
        opt.add_argument(
            "--ext",
            type=str,
            help="Force file extension (jpg/jpeg/png/webp). Optional.",
        )

    sp_url = sub.add_parser("url", help="Print a picsum.photos URL")
    add_common(sp_url)
    sp_url.set_defaults(func=cmd_url)

    sp_dl = sub.add_parser("download", help="Download image and write metadata JSON")
    add_common(sp_dl)
    sp_dl.add_argument("--out", required=True, help="Output file path (e.g. ./tmp/img.jpg)")
    sp_dl.set_defaults(func=cmd_download)

    sp_info = sub.add_parser("info", help="Fetch JSON metadata for an id or seed")
    sp_info.add_argument("--id", type=str, help="Image id")
    sp_info.add_argument("--seed", type=str, help="Seed")
    sp_info.set_defaults(func=cmd_info)

    sp_list = sub.add_parser("list", help="List images (JSON)")
    sp_list.add_argument("--page", type=_positive_int, default=1)
    sp_list.add_argument("--limit", type=_positive_int, default=30)
    sp_list.set_defaults(func=cmd_list)

    return p


def main(argv: list[str]) -> int:
    p = build_parser()
    args = p.parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

