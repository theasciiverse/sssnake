# sssnake (Asciiverse packaging)

AngelJumbo's snake that can play itself, in C with termbox2 (one header,
no libraries); packaged for the Asciiverse catalog and as system packages.
Not our code: keep changes small, list every one in PATCHES.md, and offer
fixes upstream.

- Remotes: `upstream` is github.com/AngelJumbo/sssnake, `origin` is
  github.com/theasciiverse/sssnake.
- Branch `asciiverse` = upstream master plus our commits. Tags carry the
  upstream commit's date when past a release: `v0.4.0+20261025-av.1`.
- Local static build: `docker run --rm --memory=4g -v "$PWD":/src -w /src
  alpine:3.22 sh -c "apk add gcc musl-dev && cc -O2 -static -w main.c
  autopilot.c xymap.c structs.c snake.c draw.c -o out/sssnake"` (as root,
  then chown `out/`).
- Run tests and recordings under `systemd-run --user --scope -p
  MemoryMax=4G`; the `--try-hard 2` solver costs more CPU on big boards.
- Upstream commits a built `sssnake` binary; ignore it, build into `out/`.
- No Windows build: termbox2 is POSIX only.
- Saves nothing to disk.
