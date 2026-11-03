# THIRD-PARTY-NOTICES — TRAKKCONVERTER

TRAKKCONVERTER code is MIT (`LICENSE`). The components below keep
their own licenses, in source runs AND inside the frozen exe.

| Component | License | Notes |
|---|---|---|
| PySide6 + Qt | LGPLv3 | GUI toolkit. Source: https://www.qt.io + https://pypi.org/project/PySide6/ |
| FFmpeg + FFprobe (system PATH in dev, `--add-binary` bundled in exe) | LGPLv2.1+ | Audio conversion engine. https://ffmpeg.org/download.html |
| Python stdlib (sqlite3 where used) | PSF | — |

Build tool only (not shipped): PyInstaller (GPLv2 with bootloader
exception), pytest/pytest-cov/flake8 (MIT, dev only).

Compliance: ship `LICENSE` + `NOTICE.md` + this file with the app;
LGPL texts via the links above; no Qt/FFmpeg source modification
is made by TRAKKCONVERTER.
