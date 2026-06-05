#!/usr/bin/env python3
"""
Add Pyodide Python reference cells to TGA04 semanas 1-7 (semanas 1,2,3,4,6,7).
Keeps all Cairó cells fully intact.
"""
import re, os

BASE = "/Users/diegodomingueztapia/code/tga04-neurobiz"

# ─────────────────────────────────────────────────────────────────
# CSS TO APPEND at end of existing <style> block
# ─────────────────────────────────────────────────────────────────
PYODIDE_CSS = """
    /* ══════════════════════════════════════════
       PYTHON REFERENCE CELLS (Pyodide)
    ══════════════════════════════════════════ */
    .py-section { margin: 1.5rem 0; }
    .py-section h3 {
      color: var(--primary);
      font-size: 1.05rem;
      margin-bottom: .8rem;
      display: flex;
      align-items: center;
      gap: .5rem;
    }
    .py-status {
      background: #fff8e1;
      border: 1px solid #e6c800;
      border-radius: 8px;
      padding: .5rem 1rem;
      margin-bottom: 1rem;
      font-size: .85rem;
      display: flex;
      align-items: center;
      gap: .5rem;
      color: #5d4037;
    }
    .py-status.ready { background: #e8f5e9; border-color: #43a047; color: var(--green); }
    .py-cell {
      background: #1a1a2e;
      border: 1px solid #2a2a4a;
      border-radius: 10px;
      margin-bottom: 1rem;
      overflow: hidden;
      transition: box-shadow .3s;
    }
    .py-cell:hover { box-shadow: 0 4px 16px rgba(0,0,0,.25); }
    .py-cell-header {
      display: flex;
      align-items: center;
      padding: .45rem .8rem;
      background: #16162a;
      border-bottom: 1px solid #2a2a4a;
    }
    .py-cell-idx {
      color: #6c7086;
      font-family: 'Courier New', monospace;
      font-size: .75rem;
      font-weight: 700;
      min-width: 50px;
    }
    .py-run-btn {
      background: #2e7d32;
      color: #fff;
      border: none;
      border-radius: 4px;
      padding: .2rem .65rem;
      font-size: .72rem;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: .25rem;
      transition: background .2s;
    }
    .py-run-btn:hover { background: #388e3c; }
    .py-run-btn:disabled { background: #555; cursor: not-allowed; }
    .py-cell-body {
      padding: .7rem 1rem .7rem 3.2rem;
      position: relative;
    }
    .py-cell-body::before {
      content: 'In [ ]:';
      position: absolute;
      left: .8rem;
      top: .75rem;
      color: #6c7086;
      font-family: 'Courier New', monospace;
      font-size: .78rem;
    }
    .py-cell-body.ran::before { content: 'In [*]:'; color: #89b4fa; }
    .py-cell textarea {
      width: 100%;
      min-height: 70px;
      background: transparent;
      border: none;
      color: #cdd6f4;
      font-family: 'Courier New', monospace;
      font-size: .85rem;
      line-height: 1.6;
      resize: vertical;
      outline: none;
      padding: 0;
    }
    .py-output {
      display: none;
      background: #0d0d1a;
      color: #d4d4d4;
      font-family: 'Courier New', monospace;
      font-size: .82rem;
      line-height: 1.6;
      padding: .7rem 1rem;
      max-height: 250px;
      overflow-y: auto;
      border-top: 1px solid #2a2a4a;
    }
    .py-output.visible { display: block; }
    .py-output .py-err { color: #f48771; }
    .py-ref-badge {
      display: inline-flex;
      align-items: center;
      gap: .3rem;
      background: #e8f0fe;
      color: #1a73e8;
      border-radius: 6px;
      padding: .1rem .55rem;
      font-size: .72rem;
      font-weight: 700;
    }
    .py-ref-note {
      font-size: .8rem;
      color: var(--muted);
      background: var(--light-bg);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: .6rem 1rem;
      margin-bottom: 1rem;
    }
"""

# ─────────────────────────────────────────────────────────────────
# PYODIDE SCRIPT TO APPEND before </body>
# ─────────────────────────────────────────────────────────────────
PYODIDE_SCRIPT = """
<!-- ══ PYODIDE PYTHON REFERENCE ENGINE ══ -->
<script>
// ── State ──────────────────────────────────────────────────────
var pyReady = false;
var pyLoading = false;
var pyodide = null;

function pySetStatus(msg, ready) {
  var el = document.getElementById('py-status');
  if (!el) return;
  el.textContent = msg;
  if (ready) el.classList.add('ready');
  else el.classList.remove('ready');
}

function pyDisableBtns(disabled) {
  for (var i = 1; i <= 4; i++) {
    var btn = document.getElementById('py-run-' + i);
    if (btn) btn.disabled = disabled;
  }
}

async function initPyodide() {
  if (pyReady || pyLoading) return;
  pyLoading = true;
  pyDisableBtns(true);
  pySetStatus('⏳ Cargando motor Python (Pyodide v0.24.1)...');

  try {
    var script = document.createElement('script');
    script.src = 'https://cdn.jsdelivr.net/pyodide/v0.24.1/full/pyodide.js';
    await new Promise(function(resolve, reject) {
      script.onload = resolve;
      script.onerror = function() { reject(new Error('No se pudo cargar Pyodide')); };
      document.head.appendChild(script);
    });

    if (typeof window.loadPyodide !== 'function') {
      throw new Error('loadPyodide no está definido');
    }

    pyodide = await window.loadPyodide({
      indexURL: 'https://cdn.jsdelivr.net/pyodide/v0.24.1/full/'
    });

    pyReady = true;
    pyLoading = false;
    pyDisableBtns(false);
    pySetStatus('✅ Python listo — presiona ▶ para ejecutar', true);

    // expose runner
    window._pyodideRunner = function(code) {
      return pyodide.runPythonAsync(code)
        .then(function(out) { return { output: out }; })
        .catch(function(err) { return { output: '', error: err.message || String(err) }; });
    };
  } catch(err) {
    console.error('Pyodide load error:', err);
    pyLoading = false;
    pyReady = false;
    pySetStatus('⚠️ Pyodide no disponible: ' + err.message);
    pyDisableBtns(false);
  }
}

// Auto-init on page load
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initPyodide);
} else {
  setTimeout(initPyodide, 500); // small delay to not compete with other onload
}

// ── runPyCell(n) ───────────────────────────────────────────────
window.runPyCell = async function(n) {
  if (!pyReady) {
    if (!pyLoading) { pySetStatus('⏳ Cargando Python...'); initPyodide(); }
    else pySetStatus('⏳ Python cargando, espera...');
    return;
  }

  var codeArea = document.getElementById('py-code-' + n);
  var outDiv   = document.getElementById('py-out-' + n);
  var bodyDiv  = document.getElementById('py-body-' + n);
  var runBtn   = document.getElementById('py-run-' + n);

  if (!codeArea || !outDiv) return;
  var code = codeArea.value;
  if (!code.trim()) return;

  if (runBtn) { runBtn.textContent = '⏳...'; runBtn.disabled = true; }
  outDiv.classList.add('visible');
  outDiv.querySelector('pre').textContent = '';
  if (bodyDiv) bodyDiv.classList.add('ran');

  try {
    if (!pyodide || typeof pyodide.setStdout !== 'function') {
      pyReady = false;
      throw new Error('Pyodide no listo. Recarga la página.');
    }

    var output = '';
    pyodide.setStdout({ batched: function(t) { output += t; } });
    pyodide.setStderr({ batched: function(t) { output += t; } });

    await pyodide.runPythonAsync(code);

    var pre = outDiv.querySelector('pre');
    pre.textContent = output || '(sin salida)';
    pre.className = '';
  } catch(err) {
    var pre = outDiv.querySelector('pre');
    pre.textContent = 'Error: ' + (err.message || String(err));
    pre.className = 'py-err';
  }

  if (runBtn) { runBtn.textContent = '▶ Run'; runBtn.disabled = false; }
};
</script>
"""

# ─────────────────────────────────────────────────────────────────
# PYTHON REFERENCE CONTENT PER WEEK
# Each section: header + description + N cells
# ─────────────────────────────────────────────────────────────────

WEEK_DATA = {
    1: {
        "title": "🐍 Python de Referencia — Semana 1",
        "desc": "El mismo algoritmo de <strong>Tasa de Retención</strong> escrito en Python. Compara la sintaxis Cairó con Python real.",
        "cells": [
            {
                "label": "Python — Variables y operaciones",
                "code": "# ── NeuroBiz: Calcular tasa de retención ──\n# Las variables en Python se declaran sin tipo\n# (Python infiere el tipo automáticamente)\n\nsesiones_asistidas = 847   # int (entero)\nsesiones_fallidas  = 112   # int\ntasa_retencion     = 0.78   # float (decimal)\nsede               = \"Barranquilla\"  # str (cadena)\n\n# Python usa indentación en lugar de INICIO/FIN\n# Comentarios con #\n\nprint(\"=== NeuroBiz S.A.S. — Reporte de Retención ===\")\nprint(f\"Sede: {sede}\")\nprint(f\"Sesiones asistidas: {sesiones_asistidas}\")\nprint(f\"Sesiones fallidas:  {sesiones_fallidas}\")\n\ntotal = sesiones_asistidas + sesiones_fallidas\ntasa  = sesiones_asistidas / total * 100\n\nprint(f\"Total de sesiones:  {total}\")\nprint(f\"Tasa de retención:  {tasa:.1f}%\")"
            },
            {
                "label": "Python — input() equivale a LEER",
                "code": "# ── Input en Python = LEER en Cairó ──\n# Python usa input() para entrada de datos\n# Equivale a LEER en pseudocódigo Cairó\n\nprint(\"=== Sistema de Admisión NeuroBiz ===\")\n\n# input() siempre devuelve una cadena (str)\nnombre    = input(\"Nombre del paciente: \")\nterapia   = input(\"Tipo de terapia (cognitiva/ocupacional/fonoaudiologia): \")\ndocumento = input(\"Número de documento: \")\n\n# Conversión de tipos cuando es necesario\n# int() convierte cadena a entero\n# float() convierte cadena a decimal\n\nprint(f\"\\n✔ PACIENTE REGISTRADO: {nombre}\")\nprint(f\"  Terapia asignada: {terapia}\")\nprint(f\"  Documento: {documento}\")"
            },
            {
                "label": "Python — Libre: tu primer algoritmo",
                "code": "# ── ✨ Celda libre — Escribe tu algoritmo ──\n# Practica: declara variables, usa input(), haz cálculos\n# Python es legible y no necesita punto y coma al final\n\n# Ejemplo base:\nnombre = input(\"¿Tu nombre? \")\nprint(f\"Hola, {nombre}! Bienvenido a NeuroBiz.\")\n\n# Experimenta libremente:\n# - Declara variables de distintos tipos\n# - Usa operadores aritméticos: +  -  *  /\n# - Usa print() para mostrar resultados"
            }
        ]
    },

    2: {
        "title": "🐍 Python de Referencia — Semana 2",
        "desc": "Variables y tipos de datos traducidos a Python. <strong>CADENA→str, ENTERO→int, REAL→float, BOOLEANO→bool</strong>.",
        "cells": [
            {
                "label": "Python — Declaración de variables y tipos",
                "code": "# ── Tipos de datos en Python vs Cairó ──\n# CADENA  →  str   (cadena de texto)\n# ENTERO  →  int   (número sin decimales)\n# REAL    →  float (número con decimales)\n# BOOLEANO→  bool  (True / False)\n\n# Python infiere el tipo automáticamente\n# No necesitas declarar el tipo, solo el nombre\n\nnombre_paciente   = \"Ana García\"        # str\ntipo_documento    = \"CC\"                # str\nnumero_documento  = 1043156789          # int\npeso_kg           = 62.5                # float\nsesion_activa     = True               # bool\n\nprint(f\"Paciente: {nombre_paciente}\")\nprint(f\"Documento: {tipo_documento} {numero_documento}\")\nprint(f\"Peso: {peso_kg} kg\")\nprint(f\"Sesión activa: {sesion_activa}\")\n\n# type() muestra el tipo de una variable\nprint(f\"\\nTipo de peso_kg: {type(peso_kg)}\")\nprint(f\"Tipo de sesion_activa: {type(sesion_activa)}\")"
            },
            {
                "label": "Python — Operadores aritméticos y lógicos",
                "code": "# ── Operadores en Python ──\n# Aritméticos:  +  -  *  /  // (división entera)  % (módulo)  ** (potencia)\n# Comparación:  ==  !=  <  >  <=  >=\n# Lógicos:      and  or  not\n\ntotal_sesiones = 959          # 847 + 112\ntasa_exito     = 847 / 959   # float\n\nprint(f\"Total sesiones: {total_sesiones}\")\nprint(f\"Tasa éxito: {tasa_exito:.4f}\")\n\n# Módulo y división entera\npares = total_sesiones % 2\nprint(f\"¿Total es par? {pares == 0}\")\n\n# Comparaciones lógicas (equivalen a condiciones en SI)\nSESIONES_META = 200\nprint(f\"\\nMeta semanal: {SESIONES_META}\")\nprint(f\"¿Cumple meta? {total_sesiones >= SESIONES_META}\")\nprint(f\"Sesiones sobre meta: {total_sesiones - SESIONES_META}\")"
            },
            {
                "label": "Python — Libre: Practica variables",
                "code": "# ── ✨ Celda libre — Semana 2 ──\n# Practica declarar variables de distintos tipos\n# y usar operadores\n\n# Declara tu propia versión de las variables de NeuroBiz:\n# - Nombre de paciente (str)\n# - Número de sesiones este mes (int)\n# - Tarifa por sesión (float)\n# - Está activo hoy (bool)\n\n# Luego imprime un reporte formateado\n\n# Bonus: usa f-strings (formatted strings) como arriba\n# Son más legibles que concatenar con +"
            }
        ]
    },

    3: {
        "title": "🐍 Python de Referencia — Semana 3",
        "desc": "Estructuras de control <strong>SI-SINO-SI</strong> traducidas a <strong>if-elif-else</strong> en Python.",
        "cells": [
            {
                "label": "Python — if / elif / else (equivale a SI-SINO-SI)",
                "code": "# ── if / elif / else en Python ──\n# SI condición ENTONCES ... SINO ... FSI\n# se convierte en:\n# if condición:\n#     ...\n# elif otra_condición:\n#     ...\n# else:\n#     ...\n# Nota: Python usa indentación de 4 espacios\n\ncalificacion = 78\n\nif calificacion >= 90:\n    print(f\"{calificacion} → Excelente\")\nelif calificacion >= 75:\n    print(f\"{calificacion} → Bueno\")\nelif calificacion >= 60:\n    print(f\"{calificacion} → Aceptable\")\nelse:\n    print(f\"{calificacion} → Necesita mejora\")\n\n# Operadores lógicos en condiciones\nedad = 34\nes_activo = True\n\nif edad >= 18 and es_activo:\n    print(\"Adulto activo: puede ser atendido\")\nelse:\n    print(\"No cumple requisitos de atención\")"
            },
            {
                "label": "Python — Descuento progresivo con elif",
                "code": "# ── Descuento progresivo (equivalente al ejercicio HTI) ──\nmonto_compra = 250000\n\nif monto_compra >= 500000:\n    descuento = 0.25\n    print(f\"25% de descuento (compras ≥ $500.000)\")\nelif monto_compra >= 200000:\n    descuento = 0.15\n    print(f\"15% de descuento (compras ≥ $200.000)\")\nelif monto_compra >= 100000:\n    descuento = 0.10\n    print(f\"10% de descuento (compras ≥ $100.000)\")\nelse:\n    descuento = 0\n    print(\"Sin descuento (compras < $100.000)\")\n\nmonto_final = monto_compra * (1 - descuento)\nprint(f\"\\nMonto original: ${monto_compra:,.0f}\")\nprint(f\"Descuento:     ${monto_compra * descuento:,.0f}\")\nprint(f\"Monto final:   ${monto_final:,.0f}\")"
            },
            {
                "label": "Python — Libre: Condicionales",
                "code": "# ── ✨ Celda libre — Condicionales ──\n# Escribe un algoritmo que clasifique algo\n# usando if / elif / else\n\n# Ideas:\n# - Clasificar edad de paciente (niño/adolescente/adulto/mayor)\n# - Calcular impuesto según rango de ingreso\n# - Determinar categoría de IMC (índice de masa corporal)\n\n# recuerda: Python usa indentación de 4 espacios\n# y NO usa SINO FSI — solo elif y else"
            }
        ]
    },

    4: {
        "title": "🐍 Python de Referencia — Semana 4",
        "desc": "Decisiones anidadas <strong>DD-FDD</strong> traducidas a <strong>if/elif/else</strong>. Las condiciones complejas usan <strong>and/or</strong>.",
        "cells": [
            {
                "label": "Python — SI anidado (equivale a DD-FDD)",
                "code": "# ── Decisión anidada en Python ──\n# DD (Decisión Dentro de Decisión) en Cairó\n# se replica con if dentro de otro if en Python\n\ntasa_retencion = 0.82\nsesiones_mes   = 847\n\nif sesiones_mes >= 800:\n    print(\"Alto volumen de sesiones\")\n    if tasa_retencion >= 0.80:\n        print(\"→ Terapeuta eficiente: BONO asignado\")\n    else:\n        print(\"→ Terapeuta requiere capacitación\")\nelif sesiones_mes >= 500:\n    print(\"Volumen medio\")\n    if tasa_retencion >= 0.70:\n        print(\"→ Rendimiento aceptable\")\n    else:\n        print(\"→ Mejorar atención\")\nelse:\n    print(\"Bajo volumen — revisar agenda\")"
            },
            {
                "label": "Python — Clasificar riesgo/cardiovascular",
                "code": "# ── Clasificación de riesgo (ejercicio NeuroBiz) ──\nedad      = 45\npresion   = 140  # sistólica mmHg\ncolesterol = 220  # mg/dL\n\nriesgo = \"BAJO\"\n\nif presion >= 180 or colesterol >= 240:\n    riesgo = \"MUY ALTO\"\n    print(f\"Edad: {edad}, Presión: {presion}, Colesterol: {colesterol}\")\n    print(f\"Riesgo: {riesgo} → Derivación urgente\")\nelif presion >= 140 or colesterol >= 200:\n    riesgo = \"ALTO\"\n    print(f\"Edad: {edad}, Presión: {presion}, Colesterol: {colesterol}\")\n    print(f\"Riesgo: {riesgo} → Plan de intervención\")\nelif edad > 60 and (presion >= 130 or colesterol >= 180):\n    riesgo = \"MODERADO\"\n    print(f\"Edad: {edad}, Presión: {presion}, Colesterol: {colesterol}\")\n    print(f\"Riesgo: {riesgo} → Monitoreo periódico\")\nelse:\n    print(f\"Edad: {edad}, Presión: {presion}, Colesterol: {colesterol}\")\n    print(f\"Riesgo: {riesgo} → Cuidado estándar\")"
            },
            {
                "label": "Python — Libre: Decisiones complejas",
                "code": "# ── ✨ Celda libre — Decisiones anidadas ──\n# Elige un escenario de NeuroBiz y programa\n# las reglas de decisión con if/elif/else\n\n# Ejemplo sugerido:\n# Clasificar nivel de urgencia de una sesión terapéutica\n# según: inasistencia_previa (bool), días_desde_ultima (int), es_primera_vez (bool)\n\n# Usa print() para mostrar el resultado\n# Experimenta con booleanos: and, or, not"
            }
        ]
    },

    6: {
        "title": "🐍 Python de Referencia — Semana 6",
        "desc": "El bucle <strong>MQ-FMQ</strong> (MientrasQue-FinMientrasQue) se traduce al bucle <strong>while</strong> de Python. El contador va incrementedo con <code>i += 1</code>.",
        "cells": [
            {
                "label": "Python — Bucle while (= MQ-FMQ en Cairó)",
                "code": "# ── while = MQ (Mientras Que) en Cairó ──\n# MQ condicion FMQ  →  while condicion:\n#                          ...\n#                          ...\n# Python no necesita FMQ — la indentación marca el fin\n\nprint(\"=== Contar tipos de terapia ===\")\n\n# En Cairó: cont_cognitiva = 0, cont_ocupacional = 0, cont_fono = 0\ncont_cognitiva   = 0\ncont_ocupacional = 0\ncont_fono        = 0\n\n# Simular entrada de terapias\nterapias = [\"cognitiva\", \"ocupacional\", \"cognitiva\", \"fonoaudiologia\", \"cognitiva\", \"FIN\"]\nindice   = 0\n\n# Equivale a:\n#   MQ terapias[indice] != \"FIN\" FMQ\nwhile terapias[indice] != \"FIN\":\n    t = terapias[indice]\n    if t == \"cognitiva\":\n        cont_cognitiva += 1\n    elif t == \"ocupacional\":\n        cont_ocupacional += 1\n    elif t == \"fonoaudiologia\":\n        cont_fono += 1\n    indice += 1\n\nprint(f\"Cognitiva:    {cont_cognitiva}\")\nprint(f\"Ocupacional:  {cont_ocupacional}\")\nprint(f\"Fonoaudiología: {cont_fono}\")"
            },
            {
                "label": "Python — Contadores y acumuladores con while",
                "code": "# ── Acumulador + Contador (= MQ con suma y conteo) ──\n# En Cairó:\n#   suma = 0, contador = 0\n#   MQ sesion != -1 FMQ\n#     suma = suma + sesion\n#     contador = contador + 1\n#   FMQ\n\nsesiones = [5, 8, 12, 7, 10, -1]  # -1 marca fin de entrada\nsuma      = 0\ncontador  = 0\ni         = 0\n\nwhile sesiones[i] != -1:\n    suma     += sesiones[i]    # acumulador: suma progresivamente\n    contador += 1             # contador: cuenta cuántas iteraciones\n    i        += 1\n\npromedio = suma / contador if contador > 0 else 0\n\nprint(f\"Sesiones registradas: {contador}\")\nprint(f\"Suma total: {suma}\")\nprint(f\"Promedio: {promedio:.1f}\")"
            },
            {
                "label": "Python — Libre: Practica while",
                "code": "# ── ✨ Celda libre — Bucle while ──\n# Escribe un bucle while que haga algo interesante\n\n# Ideas:\n# 1. Contar cuántos números del 1 al 20 son pares\n# 2. Simular un contador regresivo: 10, 9, 8, ... 0\n# 3. Sumar números hasta que la suma supere 100\n\n# Recuerda:\n#   i = 0\n#   while i < 10:\n#       print(i)\n#       i += 1   # sin esto → bucle infinito!\n\ni = 10\nwhile i > 0:\n    print(f\"Cuenta regresiva: {i}\")\n    i -= 1\nprint(\"¡Despegue! 🚀\")"
            }
        ]
    },

    7: {
        "title": "🐍 Python de Referencia — Semana 7",
        "desc": "<strong>HH-FHH</strong> (Hacer-Hasta que se cumpla condición) no tiene equivalente directo en Python — se usa <strong>while True: ... break</strong>. El <code>break</code> termina el bucle inmediatamente.",
        "cells": [
            {
                "label": "Python — while True / break (= HH-FHH)",
                "code": "# ── while True / break = HH-FHH en Cairó ──\n# HH\n#   instrucciones\n# FHH MIENTRAS NOT condicion\n#\n# Se traduce a:\n# while True:\n#     ...\n#     if condicion:\n#         break\n#\n# break sale del bucle inmediatamente\n\nprint(\"=== Validar duración de sesión (30-90 min) ===\")\n\nwhile True:\n    duracion = int(input(\"Duración en minutos (30-90): \"))\n    if duracion >= 30 and duracion <= 90:\n        print(f\"✔ Duración válida: {duracion} minutos\")\n        break          # equivale a FHH MIENTRAS duracion < 30 OR duracion > 90\n    else:\n        print(\"❌ Duración fuera de rango. Intenta de nuevo.\")"
            },
            {
                "label": "Python — Menú con while True/break (HH-FHH anidado)",
                "code": "# ── Menú interactivo con while True / break ──\n# Equivale al algoritmo MenuAdmisionNeuroBiz de Cairó\n\nprint(\"=== Sistema de Admisión NeuroBiz ===\")\n\nwhile True:\n    print(\"\\n1. Registrar nuevo paciente\")\n    print(\"2. Buscar paciente\")\n    print(\"3. Ver lista de espera\")\n    print(\"0. Salir\")\n\n    opcion = int(input(\"Opción: \"))\n\n    if opcion == 1:\n        nombre = input(\"Nombre del paciente: \")\n        print(f\"✔ Paciente {nombre} registrado.\")\n    elif opcion == 2:\n        print(\"Función de búsqueda no disponible aún.\")\n    elif opcion == 3:\n        print(\"Lista de espera: 5 pacientes.\")\n    elif opcion == 0:\n        print(\"Saliendo del sistema...\")\n        break          # FHH MIENTRAS opcion != 0\n    else:\n        print(\"Opción no válida. Intenta 0-3.\")"
            },
            {
                "label": "Python — Libre: HH-FHH",
                "code": "# ── ✨ Celda libre — HH-FHH ──\n# Convierte un algoritmo con HH-FHH a while True/break\n\n# Estructura:\n# while True:\n#     ... haz algo ...\n#     if condicion_de_salida:\n#         break\n#\n# El break funciona como FHH: termina el bucle\n\n# Ejercicio sugerido:\n# Menú que pida edades hasta que se ingrese 0\n# y al final muestre cuántas personas fueron registradas\n\n# O: un contador de sesiones que se detenga\n# cuando el usuario escriba 'FIN'\n\n# Experimenta con while True / break\ncontador = 0\nwhile True:\n    entrada = input(\"Escribe un número (o 'fin' para terminar): \")\n    if entrada.lower() == \"fin\":\n        break\n    contador += 1\n    print(f\"Vas {contador} registro(s)\")\nprint(f\"Total: {contador} registros\")"
            }
        ]
    }
}


def build_py_section(week_num, data):
    """Build the HTML for the Python reference section."""
    cells_html = []
    for i, cell in enumerate(data["cells"], 1):
        # Escape the Python code for HTML
        code_escaped = (cell["code"]
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;"))
        cells_html.append(f'''
      <!-- Cell {i} -->
      <div class="py-cell" id="py-cell-{i}">
        <div class="py-cell-header">
          <span class="py-cell-idx">[{i}]</span>
          <button class="py-run-btn" onclick="runPyCell({i})" id="py-run-{i}">
            ▶ Run
          </button>
        </div>
        <div class="py-cell-body" id="py-body-{i}">
          <textarea id="py-code-{i}" rows="6" spellcheck="false">{code_escaped}</textarea>
        </div>
        <div class="py-output" id="py-out-{i}"><pre></pre></div>
      </div>''')

    return f'''
<!-- ══ PYTHON REFERENCE SECTION — SEMANA {week_num} ══ -->
<div class="py-section">
  <h3>{data["title"]}</h3>
  <div class="py-ref-note">
    📌 <strong>Referencia:</strong> {data["desc"]}
    <span class="py-ref-badge">🐍 Python · Pyodide · No evaluado</span>
  </div>
  <div id="py-status" class="py-status">
    ⏳ Iniciando motor Python (Pyodide)...
  </div>
  {''.join(cells_html)}
  <div style="font-size:.78rem;color:var(--muted);margin-top:.5rem;">
    ⚡ Cada ejecución cuenta para tu aprendizaje. Código ejecutado en tu navegador — sin servidor.
  </div>
</div>
'''


def get_insertion_point_s1_to_s4(content):
    """Find the character position right after the last </section> before the quiz section."""
    # Find <section id="lab" ...> ... </section>
    # Then find the next </section> (which closes the lab section)
    # We'll insert right after that </section>

    # Alternative: find the pattern '</section>' that appears just before
    # <section id="quiz" or <section id="hti"
    # More precisely: find the last </section> before the quiz section

    # Search for the lab section
    lab_match = re.search(r'<section id="lab"', content)
    if not lab_match:
        return None

    lab_start = lab_match.start()

    # Find closing </section> of lab
    # Walk through from lab_start
    pos = lab_start
    depth = 0
    last_close = None
    while pos < len(content):
        if content[pos:pos+9] == '<section ':
            depth += 1
            pos += 9
        elif content[pos:pos+10] == '<section>':
            depth += 1
            pos += 10
        elif content[pos:pos+10] == '</section>':
            depth -= 1
            if depth == 0:
                last_close = pos + 10  # after </section>
                break
            pos += 10
        else:
            pos += 1

    return last_close


def get_insertion_point_s6_s7(content):
    """For semanas 6 and 7, find the closing </section> of the quiz section."""
    # Find <section ... id="quiz" ...> ... </section>
    quiz_match = re.search(r'<section[^>]*id="quiz"', content)
    if not quiz_match:
        return None

    pos = quiz_match.start()
    depth = 0
    last_close = None
    while pos < len(content):
        if content[pos:pos+9] == '<section ':
            depth += 1
            pos += 9
        elif content[pos:pos+10] == '<section>':
            depth += 1
            pos += 10
        elif content[pos:pos+10] == '</section>':
            depth -= 1
            if depth == 0:
                last_close = pos + 10
                break
            pos += 10
        else:
            pos += 1

    return last_close


def inject_css(content):
    """Add Pyodide CSS before the closing </style> tag."""
    # Find the last </style> tag
    last_style_close = content.rfind('</style>')
    if last_style_close == -1:
        print("  WARNING: No </style> tag found!")
        return content
    return content[:last_style_close] + PYODIDE_CSS + content[last_style_close:]


def inject_py_section(content, insert_pos, week_num, data):
    """Insert the Python reference section at insert_pos."""
    py_html = build_py_section(week_num, data)
    return content[:insert_pos] + py_html + content[insert_pos:]


def inject_py_script(content):
    """Add Pyodide script before </body>."""
    body_close = content.rfind('</body>')
    if body_close == -1:
        print("  WARNING: No </body> tag found!")
        return content
    return content[:body_close] + PYODIDE_SCRIPT + content[body_close:]


def process_week(week_num):
    filepath = os.path.join(BASE, f"semana{week_num}/index.html")
    print(f"Processing semana{week_num}...")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_len = len(content)

    # Step 1: Inject CSS
    content = inject_css(content)
    print(f"  ✓ CSS injected")

    # Step 2: Find insertion point and inject Python section
    if week_num in (1, 2, 3, 4):
        ins_pos = get_insertion_point_s1_to_s4(content)
    else:
        ins_pos = get_insertion_point_s6_s7(content)

    if ins_pos is None:
        print(f"  ERROR: Could not find insertion point for semana{week_num}")
        return

    data = WEEK_DATA[week_num]
    content = inject_py_section(content, ins_pos, week_num, data)
    print(f"  ✓ Python reference section injected at char {ins_pos}")

    # Step 3: Inject Pyodide script
    content = inject_py_script(content)
    print(f"  ✓ Pyodide script injected")

    new_len = len(content)
    print(f"  Size: {original_len:,} → {new_len:,} bytes (+{new_len - original_len:,})")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  ✓ semana{week_num} saved")


def main():
    for week in (1, 2, 3, 4, 6, 7):
        try:
            process_week(week)
        except Exception as e:
            print(f"  ERROR in semana{week}: {e}")
            import traceback
            traceback.print_exc()
    print("\nDone!")


if __name__ == "__main__":
    main()
