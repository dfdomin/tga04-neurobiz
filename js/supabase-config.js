// ══════════════════════════════════════════════════════════════
//  TGA04 · NeuroBiz S.A.S. — Configuración Supabase centralizada
//  Edita este archivo una sola vez con los datos de tu proyecto.
//  Todos los materiales del módulo lo cargan automáticamente.
// ══════════════════════════════════════════════════════════════

(function () {
  // ── EDITA ESTOS DOS VALORES ────────────────────────────────
  var SUPABASE_URL = "https://aeuimhmiwhvqeeojlfvs.supabase.co"; // Ejemplo: https://abcxyz.supabase.co
  var SUPABASE_KEY = "sb_publishable_L4AqPaDMZX42lDPNu2S2cQ_y53Cf4sP"; // Clave anon/publishable publica de Supabase
  // ──────────────────────────────────────────────────────────

  var MODULE_CODE   = "TGA04";
  var OFFERING_CODE = "TGA04-2026-2";
  var NARRATIVE     = "NeuroBiz S.A.S.";
  var COURSE_CODE   = OFFERING_CODE; // alias legacy

  if (!SUPABASE_URL || !SUPABASE_KEY) {
    console.warn(
      "[TGA04] supabase-config.js: SUPABASE_URL y SUPABASE_KEY no configurados.\n" +
      "Abre setup/CONFIGURAR_SUPABASE.html para obtener los valores."
    );
    return;
  }

  // Siempre sincronizar credenciales (evita localStorage vacío o desactualizado)
  localStorage.setItem("tga04_supabase_url", SUPABASE_URL);
  localStorage.setItem("tga04_supabase_key", SUPABASE_KEY);
  localStorage.setItem("tga04_course_code", COURSE_CODE);
  localStorage.setItem("gamif_module_code", MODULE_CODE);
  localStorage.setItem("gamif_offering_code", OFFERING_CODE);
  localStorage.setItem("gamif_narrative", NARRATIVE);

  // Exponer para gamification-sdk.js
  window.MODULE_CODE = MODULE_CODE;
  window.OFFERING_CODE = OFFERING_CODE;
  window.NARRATIVE = NARRATIVE;
  window.SUPABASE_URL = SUPABASE_URL;
  window.SUPABASE_KEY = SUPABASE_KEY;

  console.info("[TGA04] Supabase configurado ✅ →", SUPABASE_URL, "|", OFFERING_CODE);
})();
