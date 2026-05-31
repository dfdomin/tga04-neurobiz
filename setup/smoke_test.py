#!/usr/bin/env python3
"""Smoke test: verifica que todos los archivos HTML referenciados existen.

Recorre todos los .html del proyecto y revisa que cada link local
(href o src que apunte a un path relativo) corresponda a un archivo real.
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent.parent

HREF_RE = re.compile(r'(?:href|src)\s*=\s*["\'](?!https?://|mailto:|#|data:|\{|\$)([^"\']+)["\']', re.IGNORECASE)

SKIP_DIRS = {".git", "__pycache__", "backups", ".opencode"}
SKIP_FILES = {".DS_Store"}


def find_html_files(root: Path) -> list[Path]:
    files = []
    for entry in root.rglob("*.html"):
        parts = set(entry.relative_to(root).parts)
        if parts & SKIP_DIRS:
            continue
        files.append(entry)
    return sorted(files)


def check_file(html_path: Path) -> list[str]:
    errors = []
    base = html_path.parent
    try:
        content = html_path.read_text(encoding="utf-8")
    except Exception:
        errors.append(f"  ERROR: no se pudo leer {html_path}")
        return errors

    for m in HREF_RE.finditer(content):
        raw_ref = m.group(1)
        ref = urlsplit(raw_ref).path
        if "${" in ref or ref.startswith("data:"):
            continue
        if not ref:
            continue
        target = (base / ref).resolve()
        if not target.exists():
            errors.append(f"  BROKEN: {raw_ref}  (desde {html_path.relative_to(ROOT)})")
    return errors


def main() -> int:
    html_files = find_html_files(ROOT)
    total = len(html_files)
    broken = 0
    print(f"Revisando {total} archivos HTML...\n")

    for f in html_files:
        rel = f.relative_to(ROOT)
        errs = check_file(f)
        if errs:
            broken += len(errs)
            print(f"{rel}:")
            for e in errs:
                print(e)
            print()

    print(f"{'='*50}")
    print(f"Archivos revisados: {total}")
    print(f"Links rotos:        {broken}")
    return 1 if broken else 0


if __name__ == "__main__":
    raise SystemExit(main())
