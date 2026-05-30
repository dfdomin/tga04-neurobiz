// ══════════════════════════════════════════════════════════════
//  TGA04 · NeuroBiz S.A.S. — Configuración Supabase centralizada
//  Edita este archivo una sola vez con los datos de tu proyecto.
//  Todos los materiales del módulo lo cargan automáticamente.
// ══════════════════════════════════════════════════════════════

(function () {
  // ── EDITA ESTOS DOS VALORES ────────────────────────────────
  var SUPABASE_URL = "https://YOUR-PROJECT.supabase.co"; // Ejemplo: https://abcxyz.supabase.co
  var SUPABASE_KEY = "YOUR_SUPABASE_ANON_KEY"; // Tu clave anon/public de Supabase
  // ──────────────────────────────────────────────────────────

  var COURSE_CODE  = "TGA04-2026-2"; // Identificador del curso (no cambiar)

  if (!SUPABASE_URL || !SUPABASE_KEY) {
    console.warn(
      "[TGA04] supabase-config.js: SUPABASE_URL y SUPABASE_KEY no configurados.\n" +
      "Abre setup/CONFIGURAR_SUPABASE.html para obtener los valores."
    );
    return;
  }

  // Guardar en localStorage para que el tracker los use
  if (!localStorage.getItem("tga04_supabase_url")) {
    localStorage.setItem("tga04_supabase_url", SUPABASE_URL);
  }
  if (!localStorage.getItem("tga04_supabase_key")) {
    localStorage.setItem("tga04_supabase_key", SUPABASE_KEY);
  }
  if (!localStorage.getItem("tga04_course_code")) {
    localStorage.setItem("tga04_course_code", COURSE_CODE);
  }

  console.info("[TGA04] Supabase configurado ✅ →", SUPABASE_URL);
})();
