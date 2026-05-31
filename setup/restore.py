#!/usr/bin/env python3
"""Restaura datos desde un backup JSON a Supabase con migracion automatica.

Uso:
  python3 setup/restore.py setup/backups/2026-05-30_120000

Usa las mismas credenciales que backup.py (TGA04_SUPABASE_URL/TGA04_SUPABASE_KEY).
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from urllib.request import Request, urlopen


SCHEMA: dict[str, dict] = {
    "students": {
        "keep": ["cc", "name", "grupo", "horario"],
        "defaults": {
            "grupo": "",
            "horario": "",
        },
    },
    "student_progress": {
        "keep": [
            "student_id",
            "student_name",
            "grupo",
            "horario",
            "semana",
            "xp",
            "quiz_score",
            "quiz_answers",
            "hti_done",
            "activity_done",
        ],
        "defaults": {
            "grupo": "",
            "horario": "",
            "quiz_answers": {},
        },
    },
    "attendance": {
        "keep": ["cc", "fecha", "estado", "grupo"],
        "defaults": {"grupo": ""},
    },
}

TABLES = ["students", "student_progress", "attendance"]


def upsert_rows(url: str, key: str, table: str, rows: list[dict]) -> int:
    endpoint = url.rstrip("/") + f"/rest/v1/{table}"
    total = 0
    batch_size = 200
    for i in range(0, len(rows), batch_size):
        batch = rows[i : i + batch_size]
        body = json.dumps(batch).encode("utf-8")
        req = Request(
            endpoint,
            data=body,
            headers={
                "apikey": key,
                "Authorization": f"Bearer {key}",
                "Content-Type": "application/json",
                "Prefer": "resolution=merge-duplicates",
            },
            method="POST",
        )
        with urlopen(req, timeout=60) as res:
            if res.status < 200 or res.status >= 300:
                raise RuntimeError(
                    f"HTTP {res.status} al subir {table} (batch {i//batch_size + 1})"
                )
            res.read()
        total += len(batch)
    return total


def migrate(table: str, rows: list[dict]) -> list[dict]:
    keep = SCHEMA.get(table, {}).get("keep")
    defaults = SCHEMA.get(table, {}).get("defaults", {})
    if not keep:
        return rows
    out = []
    for row in rows:
        clean: dict = {}
        for col in keep:
            if col in row:
                clean[col] = row[col]
            elif col in defaults:
                clean[col] = defaults[col]
        out.append(clean)
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("backup_dir", help="Ruta al directorio del backup")
    parser.add_argument("--url", default=os.getenv("TGA04_SUPABASE_URL"))
    parser.add_argument("--key", default=os.getenv("TGA04_SUPABASE_KEY"))
    args = parser.parse_args()

    if not args.url or not args.key:
        print(
            "Falta --url/--key o variables TGA04_SUPABASE_URL/TGA04_SUPABASE_KEY",
            file=sys.stderr,
        )
        return 2

    if not os.path.isdir(args.backup_dir):
        print(f"Directorio no encontrado: {args.backup_dir}", file=sys.stderr)
        return 3

    for table in TABLES:
        path = os.path.join(args.backup_dir, f"{table}.json")
        if not os.path.isfile(path):
            print(f"  {table}.json no encontrado, saltando.")
            continue
        with open(path, encoding="utf-8") as fh:
            rows = json.load(fh)
        migrated = migrate(table, rows)
        print(f"Restaurando {table}: {len(migrated)} filas...")
        count = upsert_rows(args.url, args.key, table, migrated)
        print(f"  {count} filas subidas a Supabase.")

    print("Restauracion completa.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
