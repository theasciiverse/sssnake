# Changes from upstream

This is the Asciiverse packaging of [sssnake](https://github.com/AngelJumbo/sssnake)
by AngelJumbo (MIT), built from upstream's master as of `cc172ea` (25
October 2026): release 0.4.0 plus dajiaohuang's fix for a stack inversion
that lost its count. Upstream is the `upstream` remote; the `asciiverse`
branch carries the changes below.

## Code

- **Refuses terminals too small for a 5 by 5 board.** The `-x` and `-y`
  options already refuse less than 5, but a board sized from the terminal
  had no floor: in a terminal of 4x2 or 1x1 the game died of SIGFPE
  (`rand() % 0` placing the food), and at 2x1 it looped forever looking
  for a free cell. It now says how big the terminal must be (10 columns
  by 5 rows, 7 with `-z`). Worth offering upstream.

## Packaging (new files)

- `.github/workflows/release.yml`: av archives for Linux (static, x86-64
  and ARM64) and macOS (x86-64 and ARM64), plus SHA256SUMS, and .deb, .rpm,
  .apk and Arch packages with the man page. No Windows: termbox2 is POSIX
  only.
- `asciiverse/nfpm.yaml`: the system packages.
- `asciiverse/record-preview.py`: records the catalog preview (the
  autopilot on a walled 30 by 24 board).

## Ours

- **How to play it, at the top of README.md.** A short note on installing
  and starting it with av; the original text follows unchanged.

Upstream commits a built `sssnake` binary to its repository; our builds
replace it and do not use it.
