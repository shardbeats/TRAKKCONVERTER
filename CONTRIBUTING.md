# Contributing — TRAKKCONVERTER

Thanks for your interest. Small, focused pull requests are preferred.

## License agreement (read before contributing)

By submitting a pull request or patch to this repository you agree that
your contribution will be licensed under the repository's current code
license, **GPL-3.0-only** (see `LICENSE` and `LICENSING.md`), and that you
have the rights to submit it (you wrote it, or it is already under a
compatible license with attribution preserved).

Versions of this project published before 2026-11-23 remain MIT; new
contributions apply to the GPL-3.0-only codebase going forward.

## Trademarks

`ShardBeats`, `TRAKK` and the app icon/names are trademarks, not covered
by the code license (see `TRADEMARK.md`). Do not submit PRs that add
third-party branding.

## For the maintainer — release checklist (license part)

1. Ship `LICENSE` + `LICENSING.md` + `TRADEMARK.md` + `NOTICE.md` +
   `THIRD-PARTY-NOTICES.md` (+ `FFMPEG-BUILD-INFO.txt` where FFmpeg is bundled).
2. Keep the Qt LGPLv3 relink right and the FFmpeg GPLv3 source links alive.
3. Paste this paragraph into the release notes (fill in the build data):

> License: TRAKKCONVERTER is GPL-3.0-only for commits after the relicense point
> (see LICENSING.md; earlier releases remain MIT). Bundled FFmpeg binary
> (GPLv3, run as a separate process): <binary name>, SHA-256 <hash>.
> Corresponding source (FFmpeg release + x264/x265 + build provider files)
> available on request through this repository for at least 3 years
> from this release date.
