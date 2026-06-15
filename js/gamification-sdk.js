// ══════════════════════════════════════════════════════════════
//  Gamificación unificada · SDK compartido multi-módulo
//  Uso: GamifSDK.createPT({ semana, xpMax, visitedKey })
// ══════════════════════════════════════════════════════════════

(function (global) {
  "use strict";

  var DEFAULT_RANKS = [
    { min_xp: 650, name: "CTO" },
    { min_xp: 450, name: "Arquitecto" },
    { min_xp: 250, name: "Consultor" },
    { min_xp: 100, name: "Analista Junior" },
    { min_xp: 0, name: "Aprendiz" },
  ];

  function esc(s) {
    return String(s ?? "").replace(/[&<>"']/g, function (m) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[m];
    });
  }

  function getConfig() {
    return {
      moduleCode: global.MODULE_CODE || localStorage.getItem("gamif_module_code") || "TGA04",
      offeringCode: global.OFFERING_CODE || localStorage.getItem("gamif_offering_code") || localStorage.getItem("tga04_course_code") || "TGA04-2026-2",
      narrative: global.NARRATIVE || localStorage.getItem("gamif_narrative") || "NeuroBiz S.A.S.",
      prefix: global.GAMIF_PREFIX || "gamif",
      legacyPrefix: "tga04",
      useUnified: localStorage.getItem("gamif_use_unified") !== "false",
    };
  }

  function persistConfig(cfg) {
    localStorage.setItem("gamif_module_code", cfg.moduleCode);
    localStorage.setItem("gamif_offering_code", cfg.offeringCode);
    localStorage.setItem("gamif_narrative", cfg.narrative);
    localStorage.setItem("tga04_course_code", cfg.offeringCode);
  }

  function progressKey(cfg, semana) {
    return cfg.prefix + "_progress:" + cfg.offeringCode + ":" + semana;
  }

  function legacyProgressKey(semana) {
    return "tga04_s" + semana;
  }

  function profileKey(cfg) {
    return cfg.prefix + "_profile";
  }

  function legacyProfileKey() {
    return "tga04_global";
  }

  function sbUrl() {
    return normalizeBaseUrl(
      localStorage.getItem("tga04_supabase_url") || global.SUPABASE_URL || ""
    );
  }

  function normalizeBaseUrl(url) {
    var u = String(url || "").trim().replace(/\/+$/, "");
    u = u.replace(/\/rest\/v1\/?$/i, "");
    return u;
  }

  function sbKey() {
    return localStorage.getItem("tga04_supabase_key") || global.SUPABASE_KEY || "";
  }

  function rankFor(xp, ranks) {
    var list = ranks || DEFAULT_RANKS;
    for (var i = 0; i < list.length; i++) {
      if (xp >= list[i].min_xp) return list[i].name;
    }
    return "Aprendiz";
  }

  function riskFor(semanasVisitadas, xp) {
    if (semanasVisitadas <= 2 || xp < 80) return ["Alto", "high"];
    if (semanasVisitadas <= 5 || xp < 220) return ["Medio", "warn"];
    return ["Normal", "ok"];
  }

  function calcNotaFormativa(quizPromedio, actividades, semanas, semanasEsperadas) {
    var expected = semanasEsperadas || 13;
    var quiz = (quizPromedio / 10 * 5.0) * 0.50;
    var acts = Math.min(actividades / expected, 1) * 5.0 * 0.30;
    var sem = Math.min(semanas / expected, 1) * 5.0 * 0.20;
    return Math.round((quiz + acts + sem) * 100) / 100;
  }

  function totalXP(cfg) {
    var total = 0;
    for (var i = 0; i < localStorage.length; i++) {
      var k = localStorage.key(i);
      if (!k) continue;
      var m = k.match(/^tga04_s(\d+)$/) || k.match(/^gamif_progress:[^:]+:(\d+)$/);
      if (m) {
        try {
          total += Number(JSON.parse(localStorage.getItem(k) || "{}").xp || 0);
        } catch (e) { /* ignore */ }
      }
    }
    return total;
  }

  function loadProfile(cfg) {
    var raw = localStorage.getItem(profileKey(cfg)) || localStorage.getItem(legacyProfileKey());
    try {
      return raw ? JSON.parse(raw) : {};
    } catch (e) {
      return {};
    }
  }

  function saveProfile(cfg, profile) {
    var json = JSON.stringify(profile);
    localStorage.setItem(profileKey(cfg), json);
    localStorage.setItem(legacyProfileKey(), json);
  }

  function loadWeekState(cfg, semana) {
    var key = progressKey(cfg, semana);
    var legacy = legacyProgressKey(semana);
    var raw = localStorage.getItem(key) || localStorage.getItem(legacy);
    var state = {
      semana: semana,
      xp: 0,
      quiz_respuestas: {},
      quiz_puntaje: 0,
      nombre: "",
      cc: "",
      id_estudiante: "",
      grupo: "",
      horario: "",
      hti_entregado: false,
      hti_done: false,
      actividad_completada: false,
      activity_done: false,
    };
    try {
      if (raw) Object.assign(state, JSON.parse(raw));
    } catch (e) { /* ignore */ }
    var profile = loadProfile(cfg);
    if (!state.nombre && profile.nombre) state.nombre = profile.nombre;
    if (!state.cc && profile.cc) state.cc = profile.cc;
    if (!state.id_estudiante && profile.cc) state.id_estudiante = profile.cc;
    if (!state.grupo && profile.grupo) state.grupo = profile.grupo;
    if (!state.horario && profile.horario) state.horario = profile.horario;
    state.hti_done = !!state.hti_entregado || !!state.hti_done;
    state.activity_done = !!state.actividad_completada || !!state.activity_done;
    return state;
  }

  function saveWeekState(cfg, semana, state) {
    var json = JSON.stringify(state);
    localStorage.setItem(progressKey(cfg, semana), json);
    localStorage.setItem(legacyProgressKey(semana), json);
  }

  async function syncLegacyProgress(state, cfg) {
    var url = sbUrl();
    var key = sbKey();
    if (!url || !key) return { ok: false, reason: "no_config" };
    var res = await fetch(url + "/rest/v1/student_progress", {
      method: "POST",
      headers: {
        apikey: key,
        Authorization: "Bearer " + key,
        "Content-Type": "application/json",
        Prefer: "resolution=merge-duplicates",
      },
      body: JSON.stringify({
        student_name: state.nombre || "Anónimo",
        student_id: state.id_estudiante || state.cc || "desconocido",
        semana: state.semana,
        xp: state.xp || 0,
        quiz_answers: state.quiz_respuestas || {},
        quiz_score: state.quiz_puntaje || 0,
        hti_done: !!(state.hti_entregado || state.hti_done),
        activity_done: !!(state.actividad_completada || state.activity_done),
        grupo: state.grupo || "",
        horario: state.horario || "",
        offering_code: cfg.offeringCode,
        updated_at: new Date().toISOString(),
      }),
    });
    return { ok: res.ok || res.status === 201, status: res.status };
  }

  async function syncUnifiedProgress(state, cfg) {
    var url = sbUrl();
    var key = sbKey();
    if (!url || !key || !cfg.useUnified) return { ok: true, skipped: true };

    var cc = state.id_estudiante || state.cc;
    if (!cc) return { ok: false, reason: "no_cc" };

    var offering = encodeURIComponent(cfg.offeringCode);
    var enrollRes = await fetch(
      url + "/rest/v1/v_legacy_students?select=cc,offering_code&id=not.is.null"
      + "&cc=eq." + encodeURIComponent(cc)
      + "&offering_code=eq." + offering
      + "&limit=1",
      { headers: { apikey: key, Authorization: "Bearer " + key } }
    );
    if (!enrollRes.ok) return { ok: false, status: enrollRes.status };

    var payload = {
      offering_code: cfg.offeringCode,
      student_id: cc,
      semana: state.semana,
      xp: state.xp || 0,
      quiz_score: state.quiz_puntaje || 0,
      quiz_answers: state.quiz_respuestas || {},
      hti_done: !!(state.hti_entregado || state.hti_done),
      activity_done: !!(state.actividad_completada || state.activity_done),
      student_name: state.nombre || "",
      grupo: state.grupo || "",
      horario: state.horario || "",
    };

    var res = await fetch(url + "/rest/v1/v_legacy_student_progress", {
      method: "POST",
      headers: {
        apikey: key,
        Authorization: "Bearer " + key,
        "Content-Type": "application/json",
        Prefer: "resolution=merge-duplicates",
      },
      body: JSON.stringify(payload),
    });
    return { ok: res.ok || res.status === 201, status: res.status, unified: true };
  }

  async function callRpc(fn, payload) {
    var url = sbUrl();
    var key = sbKey();
    if (!url || !key) return { ok: false, reason: "no_config" };
    var res = await fetch(url + "/rest/v1/rpc/" + fn, {
      method: "POST",
      headers: {
        apikey: key,
        Authorization: "Bearer " + key,
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    });
    return { ok: res.ok, status: res.status };
  }

  async function syncParticipation(events, offeringCode) {
    var cfg = getConfig();
    var offering = offeringCode || cfg.offeringCode;
    if (!events || !events.length) return { ok: false, count: 0 };

    var ok = 0;
    var fail = 0;
    for (var i = 0; i < events.length; i++) {
      var ev = events[i];
      if (!ev.cc || !ev.points) continue;
      var result = await callRpc("record_participation", {
        p_cc: ev.cc,
        p_offering_code: offering,
        p_points: ev.points,
        p_event_type: ev.type || "participation",
        p_session_date: (ev.ts || new Date().toISOString()).slice(0, 10),
        p_note: ev.name || "",
      });
      if (result.ok) ok++;
      else fail++;
    }
    return { ok: fail === 0, count: ok, failed: fail };
  }

  async function syncAttendanceRows(rows, offeringCode) {
    var cfg = getConfig();
    var offering = offeringCode || cfg.offeringCode;
    if (!rows || !rows.length) return { ok: true, count: 0 };

    var ok = 0;
    var fail = 0;
    for (var i = 0; i < rows.length; i++) {
      var row = rows[i];
      if (!row.cc || !row.fecha || !row.estado || row.estado === "-") continue;
      var result = await callRpc("record_attendance", {
        p_cc: row.cc,
        p_offering_code: offering,
        p_fecha: row.fecha,
        p_estado: row.estado,
      });
      if (result.ok) ok++;
      else fail++;
    }
    return { ok: fail === 0, count: ok, failed: fail };
  }

  async function pushProgress(state, cfg, showFeedback, msgFn) {
    var cc = state.id_estudiante || state.cc;
    if (!cc || cc === "desconocido") {
      if (showFeedback) setSyncStatus("⚠️ Configura tu cédula para guardar en la nube", false);
      return { ok: false, reason: "no_cc" };
    }
    if (!sbUrl() || !sbKey()) {
      if (showFeedback) setSyncStatus("⚠️ Supabase no configurado", false);
      return { ok: false, reason: "no_config" };
    }
    if (showFeedback && msgFn) msgFn("⏳ Sincronizando…", "#fff9c4");
    try {
      var legacy = await syncLegacyProgress(state, cfg);
      var unified = await syncUnifiedProgress(state, cfg);
      var ok = legacy.ok || unified.ok;
      if (ok) setSyncStatus("✅ Guardado en la nube · " + new Date().toLocaleTimeString(), true);
      else if (showFeedback) setSyncStatus("❌ No se pudo guardar (error " + (legacy.status || unified.status || "?") + ")", false);
      if (showFeedback && msgFn) {
        if (ok) msgFn("✅ Guardado en Supabase ☁️", "lightgreen");
        else msgFn("❌ Error " + (legacy.status || unified.status || ""), "salmon");
      }
      return { ok: ok, legacy: legacy, unified: unified };
    } catch (e) {
      if (showFeedback) setSyncStatus("❌ Sin conexión · queda guardado en este dispositivo", false);
      if (showFeedback && msgFn) msgFn("❌ Sin conexión. Guardado local.", "salmon");
      return { ok: false, error: e };
    }
  }

  function detectSemanaFromPage(pt) {
    try {
      if (pt && pt.state) {
        var s = pt.state();
        if (s && s.semana) return Number(s.semana);
      }
    } catch (e) { /* ignore */ }
    var path = String((global.location && global.location.pathname) || "");
    var m = path.match(/semana(\d+)/i);
    return m ? Number(m[1]) : null;
  }

  function installAutoSync(pt, options) {
    if (!pt || pt.__gamifAutoSync) return pt;
    pt.__gamifAutoSync = true;
    var cfg = getConfig();
    var semana = (options && options.semana) || detectSemanaFromPage(pt);
    var timer = null;
    var delay = (options && options.delayMs) || 600;

    function resolveState() {
      if (options && typeof options.getState === "function") return options.getState();
      if (pt.state) return pt.state();
      if (semana) return loadWeekState(cfg, semana);
      return {};
    }

    function scheduleAutoSync() {
      if (timer) clearTimeout(timer);
      timer = setTimeout(function () {
        setSyncStatus("⏳ Guardando en la nube…");
        pushProgress(resolveState(), cfg, false).then(function (r) {
          if (!r.ok && r.reason === "no_cc") setSyncStatus("⚠️ Ingresa tu cédula para guardar en la nube", false);
        });
      }, delay);
    }

    if (pt.addXP) {
      var origAddXP = pt.addXP;
      pt.addXP = function () {
        var out = origAddXP.apply(this, arguments);
        scheduleAutoSync();
        return out;
      };
    }
    if (pt.save) {
      var origSave = pt.save;
      pt.save = function () {
        var out = origSave.apply(this, arguments);
        scheduleAutoSync();
        return out;
      };
    }

    pt.sync = async function () {
      if (pt.save) pt.save();
      return pushProgress(resolveState(), cfg, true, pt.msg);
    };

    return pt;
  }

  function enhanceWidgetUI() {
    var status = document.getElementById("pt-sync-status");
    if (!status) {
      status = document.createElement("div");
      status.id = "pt-sync-status";
      status.style.cssText = "font-size:.72rem;opacity:.9;margin-top:8px;text-align:center;line-height:1.35;";
      status.textContent = "☁️ Tu progreso se guarda solo en la nube";
      var btns = document.getElementById("pt-btns");
      if (btns) btns.parentNode.insertBefore(status, btns.nextSibling);
    }
    var saveBtn = document.getElementById("pt-btn-save");
    var advanced = document.getElementById("pt-advanced");
    if (saveBtn && advanced && !saveBtn.dataset.moved) {
      saveBtn.dataset.moved = "1";
      saveBtn.textContent = "☁️ Guardar ahora (manual)";
      saveBtn.style.width = "100%";
      saveBtn.style.marginBottom = "4px";
      advanced.insertBefore(saveBtn, advanced.firstChild);
    }
    var btnRow = document.getElementById("pt-btns");
    if (btnRow) {
      btnRow.style.flexWrap = "nowrap";
      btnRow.style.alignItems = "center";
    }
  }

  function setSyncStatus(text, ok) {
    enhanceWidgetUI();
    var status = document.getElementById("pt-sync-status");
    if (!status) return;
    status.textContent = text;
    status.style.color = ok === false ? "#ff8a80" : (ok ? "#b9f6ca" : "");
  }

  function bootPageAutoSync() {
    if (!global.PT || global.PT.__gamifAutoSync) return;
    var semana = detectSemanaFromPage(global.PT);
    enhanceWidgetUI();
    installAutoSync(global.PT, { semana: semana, quiet: true });
    var cfg = getConfig();
    var state = global.PT.state ? global.PT.state() : (semana ? loadWeekState(cfg, semana) : {});
    if (state && (state.id_estudiante || state.cc)) pushProgress(state, cfg, false);
  }

  function createPT(options) {
    var cfg = getConfig();
    persistConfig(cfg);
    var semana = options.semana;
    var xpMax = options.xpMax || 80;
    var visitedKey = options.visitedKey || ("tga04_visited_s" + semana);
    var state = loadWeekState(cfg, semana);

    function msg(text, color) {
      var el = document.getElementById("pt-msg");
      if (!el) return;
      el.textContent = text;
      el.style.color = color || "#fff";
      setTimeout(function () {
        if (el.textContent === text) el.textContent = "";
      }, options.msgTimeout || 4000);
    }

    function render() {
      var pct = Math.min((state.xp / xpMax) * 100, 100) + "%";
      var bar = document.querySelector("#pt-bar>div") || document.getElementById("pt-xp-bar");
      var cnt = document.getElementById("ptCount") || document.getElementById("pt-xp-count");
      var hBar = document.getElementById("xpBar");
      var hCnt = document.getElementById("xpCount");
      var ptRank = document.getElementById("ptRankName");
      var ptTotal = document.getElementById("ptTotal");
      var headerRank = document.getElementById("headerRank");
      if (bar) bar.style.width = pct;
      if (cnt) cnt.textContent = state.xp + " XP";
      if (hBar) hBar.style.width = pct;
      if (hCnt) hCnt.textContent = state.xp;
      var txp = totalXP(cfg);
      var rank = rankFor(txp);
      if (ptRank) ptRank.textContent = rank;
      if (ptTotal) ptTotal.textContent = txp;
      if (headerRank) headerRank.textContent = rank;
      var lbl = document.getElementById("pt-semana-label") || document.querySelector("#pt-label span");
      if (lbl) lbl.textContent = "Semana " + semana;
    }

    var autoSync = options.autoSync !== false;
    var syncTimer = null;

    function scheduleAutoSync() {
      if (!autoSync) return;
      if (syncTimer) clearTimeout(syncTimer);
      syncTimer = setTimeout(function () {
        setSyncStatus("⏳ Guardando en la nube…");
        pushProgress(state, cfg, false);
      }, options.autoSyncDelayMs || 600);
    }

    function save() {
      saveWeekState(cfg, semana, state);
      render();
      scheduleAutoSync();
    }

    function addXP(pts, motivo) {
      state.xp = Math.min((state.xp || 0) + pts, xpMax);
      msg("✨ +" + pts + " XP — " + motivo, "lime");
      save();
    }

    async function syncCloud() {
      save();
      if (!sbUrl() || !sbKey()) {
        msg("⚠️ Supabase no configurado", "orange");
        return;
      }
      await pushProgress(state, cfg, true, msg);
    }

    function exportCode() {
      save();
      var code = btoa(encodeURIComponent(JSON.stringify(state)));
      try {
        navigator.clipboard.writeText(code);
      } catch (e) { /* ignore */ }
      var a = document.createElement("a");
      a.href = "data:text/plain;charset=utf-8," + encodeURIComponent(code);
      a.download = "progreso_" + cfg.offeringCode + "_s" + semana + "_" + (state.id_estudiante || "est") + ".txt";
      a.click();
      msg("📋 ¡Código copiado!", "#fff9c4");
    }

    function importCode() {
      var code = prompt("Pega tu código de progreso:");
      if (!code) return;
      try {
        Object.assign(state, JSON.parse(decodeURIComponent(atob(code.trim()))));
        save();
        msg("✅ Progreso restaurado.", "lightgreen");
      } catch (e) {
        msg("❌ Código inválido.", "salmon");
      }
    }

    function toggle() {
      var w = document.getElementById("pt-widget");
      var t = document.getElementById("pt-toggle");
      if (w) w.classList.toggle("collapsed");
      if (t) t.textContent = w && w.classList.contains("collapsed") ? "▼" : "▲";
    }

    function init() {
      loadWeekState(cfg, semana);
      state = loadWeekState(cfg, semana);
      render();
      if (options.autoVisitXp && !localStorage.getItem(visitedKey)) {
        localStorage.setItem(visitedKey, "1");
        addXP(10, "Asistencia Semana " + semana + " ✅");
      }
      if (typeof options.onInit === "function") options.onInit(state, { addXP: addXP, save: save });
    }

    return {
      init: init,
      addXP: addXP,
      save: save,
      sync: syncCloud,
      export: exportCode,
      import: importCode,
      exportCode: exportCode,
      importCode: importCode,
      toggle: toggle,
      state: function () { return state; },
      getRank: function () { return rankFor(totalXP(cfg)); },
      totalXP: function () { return totalXP(cfg); },
      render: render,
      msg: msg,
    };
  }

  var GamifSDK = {
    esc: esc,
    getConfig: getConfig,
    persistConfig: persistConfig,
    getOfferingCode: function () { return getConfig().offeringCode; },
    rankFor: rankFor,
    riskFor: riskFor,
    calcNotaFormativa: calcNotaFormativa,
    totalXP: totalXP,
    createPT: createPT,
    installAutoSync: installAutoSync,
    pushProgress: pushProgress,
    syncParticipation: syncParticipation,
    syncAttendanceRows: syncAttendanceRows,
    callRpc: callRpc,
    loadProfile: loadProfile,
    saveProfile: saveProfile,
    loadWeekState: loadWeekState,
    loadWeekXp: function (semana, cfg) {
      var c = cfg || getConfig();
      return Number(loadWeekState(c, semana).xp || 0);
    },
    sbUrl: sbUrl,
    normalizeBaseUrl: normalizeBaseUrl,
    sbKey: sbKey,
    DEFAULT_RANKS: DEFAULT_RANKS,
  };

  global.GamifSDK = GamifSDK;
  global.rankFor = rankFor;
  global.riskFor = riskFor;

  if (typeof document !== "undefined") {
    var boot = function () {
      bootPageAutoSync();
      setTimeout(bootPageAutoSync, 200);
      setTimeout(bootPageAutoSync, 700);
    };
    if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
    else boot();
  }

})(typeof window !== "undefined" ? window : globalThis);
