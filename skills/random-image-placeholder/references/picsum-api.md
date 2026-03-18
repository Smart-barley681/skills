# Picsum Photos API quick reference

Source: `https://picsum.photos/` (Lorem Picsum).

## Core image endpoints

- Random image (w/h): `https://picsum.photos/{width}/{height}`
- Random square: `https://picsum.photos/{size}`
- Specific image by id: `https://picsum.photos/id/{id}/{width}/{height}`
- Seeded random (stable): `https://picsum.photos/seed/{seed}/{width}/{height}`

## Options (query params)

- Grayscale: `?grayscale`
- Blur: `?blur` or `?blur={1..10}`
- Cache-busting for multiple embeds: `?random=1`, `?random=2`, ...

Options can be combined, e.g.:

- `https://picsum.photos/id/870/200/300?grayscale&blur=2`

## JSON API

- List images: `https://picsum.photos/v2/list` (defaults to 30 items)
  - Pagination: `?page={n}&limit={n}`
- Image metadata by id: `https://picsum.photos/id/{id}/info`
- Seed metadata: `https://picsum.photos/seed/{seed}/info`

