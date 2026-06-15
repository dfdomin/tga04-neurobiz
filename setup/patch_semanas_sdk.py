#!/usr/bin/env python3
"""Añade gamification-sdk.js a todas las semanas y reemplaza rank inline."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SDK_TAG = '<script src="../js/gamification-sdk.js"></script>'
CONFIG_TAG = '<script src="../js/supabase-config.js"></script>'

XP_BY_WEEK = {
    1: 55, 2: 60, 3: 65, 4: 70, 6: 85, 7: 85, 8: 90, 9: 95,
    11: 90, 12: 70, 13: 75, 14: 80, 15: 70,
}


def patch_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text

    if CONFIG_TAG in text and SDK_TAG not in text:
        text = text.replace(CONFIG_TAG, CONFIG_TAG + "\n" + SDK_TAG, 1)

    text = re.sub(
        r"const rank=t=>t>=650\?'CTO':t>=450\?'Arquitecto':t>=250\?'Consultor':t>=100\?'Analista Junior':'Aprendiz'",
        "const rank=t=>GamifSDK.rankFor(t)",
        text,
    )
    text = re.sub(
        r"const rank = t => t >= 650 \? 'CTO' : t >= 450 \? 'Arquitecto' : t >= 250 \? 'Consultor' : t >= 100 \? 'Analista Junior' : 'Aprendiz'",
        "const rank = t => GamifSDK.rankFor(t)",
        text,
    )

    m = re.search(r"semana(\d+)", str(path))
    if m:
        week = int(m.group(1))
        xp = XP_BY_WEEK.get(week)
        marker = f"<!-- GAMIF_SDK_WEEK_{week} -->"
        if xp and marker not in text:
            snippet = (
                f"\n{marker}\n"
                f"<script>if(window.GamifSDK){{window.PT=window.PT||GamifSDK.createPT({{"
                f"semana:{week},xpMax:{xp},visitedKey:'tga04_visited_s{week}',autoVisitXp:false"
                f"}});}}</script>\n"
            )
            if "</body>" in text:
                text = text.replace("</body>", snippet + "</body>", 1)

    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


AUTO_SYNC_MARKER = "<!-- GAMIF_AUTO_SYNC -->"
AUTO_SYNC_SNIPPET = '''
<!-- GAMIF_AUTO_SYNC -->
<script>
(function () {
  function hook() {
    var pt = window.PT;
    if (!pt || pt.__gamifAutoHook) return;
    pt.__gamifAutoHook = true;
    var timer = null;
    function schedule() {
      if (timer) clearTimeout(timer);
      timer = setTimeout(function () {
        if (typeof pt.sync === "function") pt.sync();
      }, 700);
    }
    if (pt.addXP) {
      var origAdd = pt.addXP;
      pt.addXP = function () { var r = origAdd.apply(this, arguments); schedule(); return r; };
    }
    if (pt.save) {
      var origSave = pt.save;
      pt.save = function () { var r = origSave.apply(this, arguments); schedule(); return r; };
    }
  }
  function boot() { hook(); setTimeout(hook, 400); setTimeout(hook, 900); }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else boot();
})();
</script>
'''


def patch_auto_sync(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if AUTO_SYNC_MARKER in text:
        return False
    if "</body>" not in text or "window.PT" not in text and "const PT" not in text:
        return False
    text = text.replace("</body>", AUTO_SYNC_SNIPPET + "\n</body>", 1)
    path.write_text(text, encoding="utf-8")
    return True


def main() -> int:
    changed = 0
    synced = 0
    for path in sorted(ROOT.glob("semana*/index.html")):
        if patch_file(path):
            print(f"  patched {path.relative_to(ROOT)}")
            changed += 1
        if patch_auto_sync(path):
            print(f"  auto-sync {path.relative_to(ROOT)}")
            synced += 1
    print(f"Total: {changed} SDK, {synced} auto-sync")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
