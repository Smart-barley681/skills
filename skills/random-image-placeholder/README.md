# random-image-placeholder

Generate stable or random image placeholder URLs (and optionally download them) using [Lorem Picsum](https://picsum.photos/).

## Quick start

Generate a deterministic (seeded) URL:

```bash
python skills/random-image-placeholder/scripts/picsum.py url --seed avatar-42 --width 400 --height 400 --grayscale --blur 2
```

Download an image:

```bash
python skills/random-image-placeholder/scripts/picsum.py download --seed avatar-42 --width 120 --height 80 --out ./tmp/picsum_test.jpg
```

Fetch metadata:

```bash
python skills/random-image-placeholder/scripts/picsum.py info --id 237
```

## Requirements

- Python **3.10+** (the script uses modern type syntax)

