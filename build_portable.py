#!/usr/bin/env python3
"""Build the portable TRAKKCONVERTER (one-dir inside a ZIP).

One-dir starts instantly: nothing is extracted on launch. The portable is
shipped as a ZIP the user unzips once:

    dist\\TRAKKCONVERTER-portable-<version>.zip
        TRAKKCONVERTER\\
            TRAKKCONVERTER.exe
            _internal\\   (Qt, ffmpeg.exe + ffprobe.exe, ...)
            README.md / LICENSE / NOTICE.md / THIRD-PARTY-NOTICES.md

Usage (from the project root):
    python build_portable.py

The old `build_exe.py` produced a one-file exe that re-extracted ~200 MB to
%TMP% on EVERY launch; it was removed on purpose.
"""
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
APP_NAME = "TRAKKCONVERTER"
ICON_NAME = "icon.ico"
EXE_DIR = ROOT / "dist" / "portable" / APP_NAME
DOCS = ("README.md", "LICENSE", "NOTICE.md", "THIRD-PARTY-NOTICES.md")


def find_ffmpeg() -> list[str]:
    """Locate ffmpeg.exe and ffprobe.exe on this machine."""
    ffmpeg = shutil.which("ffmpeg")
    ffprobe = shutil.which("ffprobe")
    if not ffmpeg or not ffprobe:
        print("WARNING:")
        print("  ffmpeg/ffprobe not found on PATH, so the build will NOT be portable.")
        print("  Install FFmpeg first (https://ffmpeg.org/download.html) and add its bin/ to PATH.")
        return []
    return [ffmpeg, ffprobe]


def project_version() -> str:
    """Single source: setup.py (regex, no import needed)."""
    text = (ROOT / "setup.py").read_text(encoding="utf-8")
    m = re.search(r'version\s*=\s*"([^"]+)"', text)
    return m.group(1) if m else "dev"


def main() -> int:
    version = project_version()
    print("=" * 70)
    print(f"Building {APP_NAME} portable (one-dir + ZIP), version {version} ...")
    print("=" * 70)

    try:
        import PyInstaller  # noqa: F401
    except ImportError:
        print("PyInstaller not installed. Installing ...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"],
                       check=True)

    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--noconfirm", "--clean",
        "--onedir",
        "--windowed",
        "--name", APP_NAME,
        "--distpath", "dist/portable",
        "--workpath", "build/portable",
        "--specpath", "build/portable",
        "--add-data", f"{ROOT / 'styles.qss'};.",
    ]

    for binary in find_ffmpeg():
        cmd += ["--add-binary", f"{binary};."]
        print(f"  Bundling: {binary}")

    icon = ROOT / ICON_NAME
    if icon.exists():
        cmd += ["--icon", str(icon), "--add-data", f"{icon};."]
        print(f"  Icon: {icon}")
    else:
        print("  WARNING: no icon.ico found; using default PyInstaller icon.")

    cmd.append(str(ROOT / "main.py"))

    if EXE_DIR.exists():
        shutil.rmtree(EXE_DIR, ignore_errors=True)
    print("\nRunning:")
    print("  " + " ".join(cmd))
    subprocess.run(cmd, check=True, cwd=ROOT)

    exe = EXE_DIR / f"{APP_NAME}.exe"
    if not exe.is_file():
        print("ERROR: compiled exe not found in dist/portable/")
        return 1

    for name in DOCS:
        src = ROOT / name
        if src.is_file():
            shutil.copy2(src, EXE_DIR / name)

    out = ROOT / "dist" / f"{APP_NAME}-portable-{version}.zip"
    if out.exists():
        out.unlink()
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
        for p in sorted(EXE_DIR.rglob("*")):
            if p.is_file():
                zf.write(p, Path(APP_NAME) / p.relative_to(EXE_DIR))

    print("=" * 70)
    print(f"BUILD OK: {out} ({out.stat().st_size / 1e6:.1f} MB)")
    print(f"Unzip once, then run {APP_NAME}\\{APP_NAME}.exe.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
