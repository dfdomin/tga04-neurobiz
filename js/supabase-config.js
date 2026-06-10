// ══════════════════════════════════════════════════════════════
//  TGA04 · NeuroBiz S.A.S. — Configuración Supabase (gamificación)
// ══════════════════════════════════════════════════════════════

(function () {
  var SUPABASE_URL = "https://aeuimhmiwhvqeeojlfvs.supabase.co";
  var SUPABASE_KEY = "sb_publishable_L4AqPaDMZX42lDPNu2S2cQ_y53Cf4sP";

  var MODULE_CODE   = "TGA04";
  var OFFERING_CODE = "TGA04-2026-2";
  var NARRATIVE     = "NeuroBiz S.A.S.";
  var COURSE_CODE   = OFFERING_CODE;

  if (!SUPABASE_URL || !SUPABASE_KEY) {
    console.warn("[TGA04] supabase-config.js: credenciales no configuradas.");
    return;
  }

  localStorage.setItem("tga04_supabase_url", SUPABASE_URL);
  localStorage.setItem("tga04_supabase_key", SUPABASE_KEY);
  localStorage.setItem("gamif_module_code", MODULE_CODE);
  localStorage.setItem("gamif_offering_code", OFFERING_CODE);
  localStorage.setItem("gamif_narrative", NARRATIVE);
  localStorage.setItem("tga04_course_code", COURSE_CODE);

  window.MODULE_CODE = MODULE_CODE;
  window.OFFERING_CODE = OFFERING_CODE;
  window.NARRATIVE = NARRATIVE;
  window.SUPABASE_URL = SUPABASE_URL;
  window.SUPABASE_KEY = SUPABASE_KEY;
  window.GAMIF_PREFIX = "tga04";

  console.info("[TGA04] Supabase gamificación ✅ →", SUPABASE_URL, "|", OFFERING_CODE);
})();
