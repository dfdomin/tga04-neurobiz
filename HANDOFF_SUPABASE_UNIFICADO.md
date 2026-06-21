# Handoff — Supabase unificado IUB + consola docente

**Fecha:** 2026-06-15  
**Para:** Hermes (u otro agente en sesión nueva)  
**Usuario:** Diego — Profesor TGA04/TGA05/ADM18/TD, IUB NeuroBiz  
**Repo principal TGA04:** `FundamentosComputacion` → GitHub `dfdomin/tga04-neurobiz`  
**Directorio local:** `/Users/diegodomingueztapia/Library/CloudStorage/OneDrive-Unibarranquilla/DiegoIcloud/2026/copilot/FundamentosComputacion`

**Ubicación de este archivo (para Hermes):** `FundamentosComputacion/HANDOFF_SUPABASE_UNIFICADO.md` (raíz del repo, junto a `HANDOFF_3_DOCUMENTOS.md`). Copia espejo: `.hermes/HANDOFF_SUPABASE_UNIFICADO.md`.

**Docs relacionados:** `setup/IUB_SUPABASE_COMPARTIDO.md`, `KNOWLEDGE_BASE.md`

---

## 1. Objetivo que persigue Diego

**Un solo proyecto Supabase** para todos los módulos y cuatrimestres. No crear un Supabase nuevo por curso.

- Módulos: **TGA04**, **TGA05**, **ADM18**, **TD**
- Cada cuatrimestre = fila en `course_offerings` (ej. `TGA04-2026-2`), no un proyecto distinto
- Un solo login docente para participación, asistencia y notas (consola **iub-docente**, en progreso)

---

## 2. Supabase consolidado (fuente de verdad hoy)

| Campo | Valor |
|-------|--------|
| **URL API** | `https://nnrgxuzvjtweyzkdrech.supabase.co` |
| **Project ref** | `nnrgxuzvjtweyzkdrech` |
| **Nombre en dashboard** | `adm18-latambox` (solo cosmético; renombrarlo **no** rompe nada) |
| **Panel** | https://supabase.com/dashboard/project/nnrgxuzvjtweyzkdrech |

**Importante:** El email de la cuenta Supabase **no** está documentado en el repo. Diego tiene **3 cuentas**; el proyecto se encuentra buscando `adm18-latambox` o abriendo el enlace directo del ref arriba en cada cuenta.

**Publishable key** (pública, en git): ver `js/supabase-config.js` o `setup/iub-supabase-shared.json`.  
**Service role** (migraciones): solo en `.env` local (`GAMIF_SUPABASE_KEY`) — **nunca commitear**.

---

## 3. Proyectos Supabase históricos (ya no usar en producción)

| Proyecto | Ref | Rol |
|----------|-----|-----|
| TGA04 viejo | `aeuimhmiwhvqeeojlfvs` | Origen con tablas `students`, `student_progress`. **Migrado** al consolidado. |
| TGA05 viejo | `hmaognhkhyvbjxqznnhx` | Origen EstructuraDatos. DNS caído/pausado. **Migrado** al consolidado. |
| **IUB unificado** | `nnrgxuzvjtweyzkdrech` | **Oficial** para ADM18 + TGA04 + TGA05 + TD |

---

## 4. Modelo de datos unificado (cómo funciona)

### 4.1 Tablas reales (donde viven los datos)

```
modules              → TGA04, TGA05, ADM18, TD
course_offerings     → TGA04-2026-2, TGA05-2026-2, ADM18-2026-2, TD-2026-2
people               → estudiantes por cédula (cc)
enrollments          → persona inscrita en un offering (grupo, horario)
periods + activities → semanas del curso (slug weekly_summary, quiz, etc.)
activity_completions → progreso semanal (XP, quiz, actividades) ← núcleo gamificación
xp_ledger            → historial de puntos
enrollment_attendance→ asistencia P/T/F/M/I
participation_events → participación en clase (+1/+3/+5)
teacher_accounts     → login docente (RPC verify_teacher_login)
```

### 4.2 Vistas “legacy” (compatibilidad con dashboards viejos)

En el consolidado **NO existen** las tablas físicas `student_progress` ni `students` → **HTTP 404 es normal**.

| Viejo endpoint | Reemplazo en unificado |
|----------------|------------------------|
| `GET /student_progress` | `GET /v_legacy_student_progress?offering_code=eq.TGA04-2026-2` |
| `GET /students` | `GET /v_legacy_students?offering_code=eq.TGA04-2026-2` |
| Resumen docente | `GET /v_legacy_resumen_docente?offering_code=eq.…` |
| Asistencia | `GET /v_legacy_attendance?offering_code=eq.…` |

Las vistas leen de `activity_completions` + `people` + `enrollments`. DDL: `schema/gamification_unified.sql`.

### 4.3 Escritura (estudiantes guardan progreso)

- **Correcto:** RPC `upsert_weekly_progress` vía `js/gamification-sdk.js` (`GamifSDK.syncWeekProgress`, `scheduleCloudPush`)
- **Incorrecto en unificado:** `POST /rest/v1/student_progress` (tabla no existe → falla)

Algunas páginas de semana TGA04 aún tienen código legacy que hace POST a `student_progress`; el SDK unificado en `gamification-sdk.js` ya soporta el RPC.

---

## 5. Offerings y conteos (post-migración, verificado)

| Offering | enrollments (aprox.) | activity_completions (aprox.) |
|----------|----------------------|-------------------------------|
| TGA04-2026-2 | 57 | 71 |
| TGA05-2026-2 | 41 | 30 |
| ADM18-2026-2 | 39 | 1 |

Migraciones ejecutadas por Diego con:

```bash
cd FundamentosComputacion
set -a && source .env && set +a
python3 setup/backup_all_modules.py --source TGA04   # backup previo
python3 setup/migrate_modules.py --import-tga04
python3 setup/migrate_modules.py --import-tga05
python3 setup/migrate_modules.py --verify-only
```

Scripts: `setup/migrate_modules.py`, `setup/modules.json`, `setup/backup_all_modules.py`.  
Docs: `setup/IUB_SUPABASE_COMPARTIDO.md`, `setup/iub-supabase-shared.json`.

**TGA04:** 5 filas del origen no migraron (datos de prueba: `desconocido`, `TEST_SYNC_999`).  
**TGA05:** `student_attempts` no existía en origen → 0 intentos de ejercicios migrados.

---

## 6. Repos, GitHub Pages y configs

| Módulo | Repo GitHub | Pages | `MODULE_CODE` | `OFFERING_CODE` |
|--------|-------------|-------|---------------|-----------------|
| TGA04 | dfdomin/tga04-neurobiz | https://dfdomin.github.io/tga04-neurobiz/ | TGA04 | TGA04-2026-2 |
| TGA05 | dfdomin/tga05-neurobiz | https://dfdomin.github.io/tga05-neurobiz/ | TGA05 | TGA05-2026-2 |
| ADM18 | (ProcesamientoInformacion / LatamBox) | adm18-latambox | ADM18 | ADM18-2026-2 |
| TD | td-inteligencia-negocios | https://dfdomin.github.io/td-inteligencia-negocios/ | TD | TD-2026-2 |

Todos los `js/supabase-config.js` activos apuntan a **`nnrgxuzvjtweyzkdrech`** con la misma publishable key.

### Dashboards docente (estado)

- **`dashboard/participacion.html`**: triplicado por repo (tga04_, tga05_, adm18_ en localStorage). Lee `v_legacy_students`, escribe con `GamifSDK`. Login: `teacher-auth.js` + `verify_teacher_login`.
- **`dashboard/notas.html` TGA04**: lee `student_progress` **o** `v_legacy_student_progress` + pestaña «Para Excel».
- **`dashboard/notas.html` TGA05**: actualizado para `v_legacy_*`; PIN visible eliminado → login docente Supabase (commit `bd3a3f5`).
- **`dashboard/revision.html` TGA05**: aún puede tener PIN legacy — pendiente alinear.

### Consola unificada (Opción A — publicada ✅)

Carpeta local: `FundamentosComputacion/iub-docente/`
**URL:** https://dfdomin.github.io/iub-docente/

- `index.html` — login único + selector de módulo (`js/module-context.js`)
- `participacion.html` — clase en vivo, asistencia, historial, validar semana, reporte
- `profesor.html` — dashboard docente con XP, quiz, actividades y asistencia reglamentaria ✅ NUEVO
- `notas.html` — consolidador de notas formativas (resumen + detalle para Excel) ✅ NUEVO
- Login: `teacher-auth.js` + RPC `verify_teacher_login` (sin PIN en pantalla)
- Catálogo de módulos en `module-context.js` (TD corregido: Transformación Digital, sitio td-inteligencia-negocios)
- **Todas las páginas** usan `IUBModuleContext.requireSelected()` para el offering dinámico

---

## 7. Autenticación docente

- Tabla: `teacher_accounts` (migración `setup/migrations/008_teacher_auth_and_groups.sql`)
- RPC: `verify_teacher_login(p_username, p_password)`
- Cuenta seed: usuario `docente` con acceso a módulos `['ADM18','TGA04','TGA05','TD']`
- Frontend: `js/teacher-auth.js` — sesión 8 h en `sessionStorage` (`iub_teacher_session`)
- **No** usar PIN en pantalla (`tga05`, etc.); contraseña solo en Supabase

---

## 8. Qué está “solucionado” vs qué falta

### ✅ Hecho

- Un solo Supabase configurado en producción (Pages) para TGA04/TGA05/TD
- Migración de datos TGA04 y TGA05 al consolidado
- Daniela Aguilar y estudiantes visibles en `notas.html` vía vista legacy
- `migrate_modules.py` con upsert `on_conflict` (re-ejecutable)
- Documentación `setup/IUB_SUPABASE_COMPARTIDO.md`
- Esqueleto `iub-docente` con login + selector de módulo
- **`iub-docente` publicado** en GitHub Pages ✅ (https://dfdomin.github.io/iub-docente/)
- **`profesor.html` y `notas.html`** portados a `iub-docente/` como páginas multi-módulo ✅
- **Todas las semanas de TGA04 y TGA05** corregidas para usar `v_legacy_students` (no la tabla `students` que daba 404) ✅
- **Auto-verificación de cédula** en todas las semanas: si la cc guardada en localStorage existe en la DB, el modal de identificación no aparece ✅

### ⚠️ Gaps conocidos

1. **`student_progress` / `students` dan 404** en unificado — **esperado**; usar vistas o tablas nuevas (sección 4). Las semanas de TGA04 y TGA05 ya están corregidas.
2. **Algunas semanas** aún POSTean a `student_progress` sin pasar por SDK (revisar semanas que no se migraron).
3. **`dashboard/revision.html` TGA05** puede tener PIN legacy — pendiente alinear con login docente.
4. **Solo 2 filas** en `v_legacy_student_progress` sin filtro `offering_code` — consultar siempre con `?offering_code=eq.TGA04-2026-2`.

---

## 9. Comandos útiles para Hermes

```bash
# Verificar offerings en consolidado
cd FundamentosComputacion && set -a && source .env && set +a
python3 setup/migrate_modules.py --verify-only

# Probar consola local
cd iub-docente && python3 -m http.server 8090
# → http://localhost:8090/

# SQL en Supabase (Table Editor o SQL Editor)
select code from course_offerings;
select co.code, count(*) from activity_completions ac
  join course_offerings co on co.id = ac.offering_id group by co.code;
select * from v_legacy_student_progress
  where offering_code = 'TGA04-2026-2' limit 10;
```

---

## 10. Archivos clave (referencia, no duplicar contenido)

| Path | Propósito |
|------|-----------|
| `schema/gamification_unified.sql` | DDL tablas + vistas legacy + RPCs |
| `setup/migrations/003_tga04_seed_and_rpc.sql` | Seed TGA04 + upsert_weekly_progress |
| `setup/migrations/006_tga05_seed_and_periods.sql` | Seed TGA05 |
| `setup/migrations/007_td_seed_and_periods.sql` | Seed TD (repo TD/) |
| `setup/migrations/008_teacher_auth_and_groups.sql` | Login docente |
| `js/gamification-sdk.js` | SDK escritura/lectura unificada |
| `js/supabase-config.js` | URL + MODULE_CODE + OFFERING_CODE por repo |
| `js/teacher-auth.js` | Sesión docente |
| `dashboard/participacion.html` | Clase en vivo, asistencia, importar estudiantes |
| `dashboard/notas.html` | Consolidación notas formativas |
| `iub-docente/` | Consola docente unificada (WIP) |
| `.env` (local, gitignored) | GAMIF_SUPABASE_*, TGA04_SUPABASE_* para migraciones |

Handoff anterior (obsoleto en Supabase URL): `.hermes/HANDOFF_2026-06-01.md` — referencia `aeuimhmi…` **ya reemplazada**.

---

## 11. Nuevo cuatrimestre (sin nuevo Supabase)

1. SQL: insert en `course_offerings` (ej. `TGA04-2027-1`) + `periods`.
2. En cada repo estudiante: cambiar solo `OFFERING_CODE` en `supabase-config.js`.
3. En `iub-docente/js/module-context.js`: añadir offering al catálogo si aplica.

---

## 12. Próximos pasos (actualizado 2026-06-21)

1. **✅ `iub-docente` publicado** en GitHub Pages — https://dfdomin.github.io/iub-docente/
2. **✅ `profesor.html` y `notas.html`** portados a la consola única con soporte multi-módulo.
3. **✅ Todas las semanas de TGA04 y TGA05** corregidas para usar `v_legacy_students` con auto-verificación de cédula.
4. Pendiente: **`dashboard/revision.html` TGA05** — migrar a login docente (sin PIN).
5. Pendiente: **Verificar semanas no migradas** — algunas semanas de TGA04 (semana5, semana10) no tenían el modal de identificación ni el SDK; confirmar si necesitan actualización.
6. Pendiente: **Copiar `HANDOFF_SUPABASE_UNIFICADO.md`** a `~/.hermes/HANDOFF_SUPABASE_UNIFICADO.md` para que Hermes lo cargue automáticamente.

---

## 13. Skills sugeridos para el agente

| Skill / acción | Cuándo usarla |
|----------------|---------------|
| `handoff` | Actualizar este doc al cerrar otra sesión larga |
| `learn-codebase` / explore | Navegar repos TGA05, ADM18, TD en `copilot/` |
| `writing-plans` + `executing-plans` | Publicar iub-docente y migrar dashboards |
| `verification-before-completion` | Antes de afirmar “migración OK” — correr `--verify-only` y query SQL |
| `systematic-debugging` | Si 404/0 estudiantes — distinguir tabla vs vista vs offering_code |
| `setup-pre-commit` | Si se commitean scripts de migración |

---

## 14. Glosario rápido

| Término | Significado |
|---------|-------------|
| **Offering** | Instancia del curso en un cuatrimestre (`TGA04-2026-2`) |
| **Module** | Asignatura (`TGA04`) |
| **v_legacy_*** | Vista SQL que imita tablas viejas para el frontend |
| **404 en student_progress** | Normal en consolidado; no es bug de migración |
| **GamifSDK** | `js/gamification-sdk.js` — cliente unificado |
| **Hermes** | Agente/sesión que continúa trabajo con este handoff |

---

*Credenciales sensibles omitidas a propósito. Usar `.env` local y Supabase Dashboard → Project Settings → API.*
