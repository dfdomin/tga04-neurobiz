#!/usr/bin/env python3
"""Exporta progreso TGA04 desde Supabase a CSV.

Uso:
  python3 setup/exportar_notas.py --url https://xxx.supabase.co --key sb_publishable_...

Si no pasas argumentos, lee TGA04_SUPABASE_URL y TGA04_SUPABASE_KEY del entorno.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
from collections import defaultdict
from datetime import datetime
from urllib.request import Request, urlopen


def fetch_progress(url: str, key: str) -> list[dict]:
    rows: list[dict] = []
    offset = 0
    limit = 1000
    while True:
        endpoint = (
            url.rstrip("/")
            + f"/rest/v1/student_progress?select=*&limit={limit}&offset={offset}"
        )
        req = Request(endpoint, headers={"apikey": key, "Authorization": f"Bearer {key}"})
        with urlopen(req, timeout=30) as res:
            if res.status < 200 or res.status >= 300:
                raise RuntimeError(
                    f"HTTP {res.status} al descargar student_progress (offset={offset})"
                )
            chunk = json.loads(res.read().decode("utf-8"))
        if not chunk:
            break
        rows.extend(chunk)
        if len(chunk) < limit:
            break
        offset += limit
    return rows


def consolidate(rows: list[dict], expected_weeks: int) -> list[dict]:
    grouped: dict[str, dict] = {}
    for row in rows:
        sid = row.get("student_id") or row.get("student_name") or "desconocido"
        item = grouped.setdefault(
            sid,
            {
                "student_id": sid,
                "student_name": row.get("student_name") or "Anonimo",
                "grupo": row.get("grupo") or "",
                "semanas": set(),
                "quiz_sum": 0.0,
                "quiz_count": 0,
                "actividades": 0,
                "xp_total": 0,
            },
        )
        item["student_name"] = row.get("student_name") or item["student_name"]
        item["grupo"] = row.get("grupo") or item["grupo"]
        if row.get("semana"):
            item["semanas"].add(int(row["semana"]))
        item["quiz_sum"] += float(row.get("quiz_score") or 0)
        item["quiz_count"] += 1
        item["xp_total"] += int(row.get("xp") or 0)
        if row.get("activity_done") or row.get("hti_done"):
            item["actividades"] += 1

    output = []
    for item in grouped.values():
        quiz_avg = min(item["quiz_sum"] / item["quiz_count"], 10) if item["quiz_count"] else 0.0
        nota = (
            (quiz_avg / 10 * 5.0) * 0.50
            + (min(item["actividades"] / expected_weeks, 1) * 5.0) * 0.30
            + (min(len(item["semanas"]) / expected_weeks, 1) * 5.0) * 0.20
        )
        output.append(
            {
                "student_name": item["student_name"],
                "student_id": item["student_id"],
                "grupo": item["grupo"],
                "semanas_visitadas": len(item["semanas"]),
                "xp_total": item["xp_total"],
                "quiz_promedio_10": round(quiz_avg, 2),
                "actividades": item["actividades"],
                "nota_formativa_5": round(nota, 2),
            }
        )
    return sorted(output, key=lambda x: (x["grupo"], x["student_name"]))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default=os.getenv("TGA04_SUPABASE_URL"))
    parser.add_argument("--key", default=os.getenv("TGA04_SUPABASE_KEY"))
    parser.add_argument("--expected-weeks", type=int, default=13)
    parser.add_argument("--output", default="")
    args = parser.parse_args()

    if not args.url or not args.key:
        print("Falta --url/--key o variables TGA04_SUPABASE_URL/TGA04_SUPABASE_KEY", file=sys.stderr)
        return 2

    rows = consolidate(fetch_progress(args.url, args.key), args.expected_weeks)
    output = args.output or f"Reporte_Notas_TGA04-{datetime.now().strftime('%Y%m%d-%H%M')}.csv"
    with open(output, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()) if rows else [
            "student_name", "student_id", "grupo", "semanas_visitadas", "xp_total",
            "quiz_promedio_10", "actividades", "nota_formativa_5",
        ])
        writer.writeheader()
        writer.writerows(rows)
    print(f"Exportado: {output} ({len(rows)} estudiantes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
