# Supabase compartido IUB — todos los módulos

**Un solo proyecto** para ADM18, TGA04, TGA05 y TD.

| Campo | Valor |
|-------|-------|
| Proyecto | `adm18-latambox` |
| Ref | `nnrgxuzvjtweyzkdrech` |
| URL | `https://nnrgxuzvjtweyzkdrech.supabase.co` |
| Publishable key | `sb_publishable_-101J7EEEhv-C5kjosWGTg_657OtsBg` |

## Offerings por módulo

| Módulo | `MODULE_CODE` | `OFFERING_CODE` |
|--------|---------------|-----------------|
| ADM18 (LatamBox) | `ADM18` | `ADM18-2026-2` |
| TGA04 (NeuroBiz) | `TGA04` | `TGA04-2026-2` |
| TGA05 (NeuroBiz) | `TGA05` | `TGA05-2026-2` |
| TD (Mercado360) | `TD` | `TD-2026-2` |

## SQL (orden en el proyecto remoto)

1. `setup/gamification_unified.sql` — esquema base (una sola vez)
2. `setup/migrations/003_adm18_seed_and_rpc.sql`
3. `setup/migrations/004_adm18_roster_rpc.sql`
4. `setup/migrations/005_adm18_attendance_states.sql`
5. `setup/migrations/006_tga05_seed_and_periods.sql`
6. Seeds TGA04: `tga04-neurobiz/setup/migrations/003_tga04_seed_and_rpc.sql` (ya aplicado si hay 13+ periodos)

## Ejecutar SQL desde terminal (repo ADM18)

```bash
cd ProcesamientoInformacion
supabase link --project-ref nnrgxuzvjtweyzkdrech
supabase db query --linked -f setup/migrations/006_tga05_seed_and_periods.sql
```

## Frontend

Cada repo tiene `js/supabase-config.js` con la **misma URL/key** y su propio `MODULE_CODE` / `OFFERING_CODE`.

## Migración desde proyectos viejos (jun 2026)

| Origen (retirado) | Ref | Destino oficial |
|-------------------|-----|-----------------|
| TGA04 NeuroBiz solo | `aeuimhmiwhvqeeojlfvs` | `nnrgxuzvjtweyzkdrech` |
| TGA05 (EstructuraDatos) | `hmaognhkhyvbjxqznnhx` (pausado/eliminado — ver abajo) | `nnrgxuzvjtweyzkdrech` |

**TGA04:** migrado con `python3 setup/backup_all_modules.py --source TGA04` y `python3 setup/migrate_modules.py --import-tga04`. Los 53 estudiantes reales y 51 registros de progreso están en `activity_completions` bajo `TGA04-2026-2`. Cinco filas del origen eran pruebas (`desconocido` / `TEST_SYNC_999`) y se omitieron a propósito.

**TGA05:** requiere en `.env` las variables `TGA05_SUPABASE_URL` y `TGA05_SUPABASE_KEY` del proyecto origen, luego:

```bash
set -a && source .env && set +a
python3 setup/backup_all_modules.py --source TGA05
python3 setup/migrate_modules.py --import-tga05
```

Si TGA05 ya guardaba directo en el consolidado, no hace falta importar.

**No usar** el proyecto `aeuimhmiwhvqeeojlfvs` para el curso en vivo; solo archivo histórico.

## Nuevo cuatrimestre (sin nuevo Supabase)

1. SQL: insertar fila en `course_offerings` (ej. `TGA04-2027-1`) y sus `periods`.
2. En cada repo: cambiar solo `OFFERING_CODE` en `js/supabase-config.js`.
3. Mismo `SUPABASE_URL` y `SUPABASE_KEY` siempre.
