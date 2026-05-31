#!/usr/bin/env python3
"""Descarga todas las tablas Supabase a JSON con timestamp.

Uso:
  python3 setup/backup.py --url https://xxx.supabase.co --key sb_publishable_...

Si no pasas argumentos, lee TGA04_SUPABASE_URL y TGA04_SUPABASE_KEY del entorno.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime
from urllib.request import Request, urlopen


TABLES = ["students", "student_progress", "attendance"]


def fetch_table(url: str, key: str, table: str) -> list[dict]:
    rows: list[dict] = []
    offset = 0
    limit = 1000
    while True:
        endpoint = (
            url.rstrip("/")
            + f"/rest/v1/{table}?select=*&limit={limit}&offset={offset}"
        )
        req = Request(
            endpoint,
            headers={"apikey": key, "Authorization": f"Bearer {key}"},
        )
        with urlopen(req, timeout=30) as res:
            if res.status < 200 or res.status >= 300:
                raise RuntimeError(
                    f"HTTP {res.status} al descargar {table} (offset={offset})"
                )
            chunk = json.loads(res.read().decode("utf-8"))
        if not chunk:
            break
        rows.extend(chunk)
        if len(chunk) < limit:
            break
        offset += limit
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default=os.getenv("TGA04_SUPABASE_URL"))
    parser.add_argument("--key", default=os.getenv("TGA04_SUPABASE_KEY"))
    args = parser.parse_args()

    if not args.url or not args.key:
        print(
            "Falta --url/--key o variables TGA04_SUPABASE_URL/TGA04_SUPABASE_KEY",
            file=sys.stderr,
        )
        return 2

    ts = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    out_dir = os.path.join(os.path.dirname(__file__), "backups", ts)
    os.makedirs(out_dir, exist_ok=True)

    for table in TABLES:
        print(f"Descargando {table}...")
        try:
            rows = fetch_table(args.url, args.key, table)
        except Exception as exc:
            print(f"  ERROR en {table}: {exc}", file=sys.stderr)
            return 3
        path = os.path.join(out_dir, f"{table}.json")
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(rows, fh, ensure_ascii=False, indent=2)
        print(f"  {len(rows)} filas → {path}")

    print(f"Backup completo en {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
