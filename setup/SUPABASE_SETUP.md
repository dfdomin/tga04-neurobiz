# Configuración Supabase — TGA04 (NeuroBiz)

Proyecto: `https://aeuimhmiwhvqeeojlfvs.supabase.co`  
Offering: `TGA04-2026-2`

## Scripts SQL (en orden)

1. `setup/migrations/000_preserve_tga04_legacy.sql`
2. `setup/gamification_unified.sql`
3. `setup/migrations/003_tga04_seed_and_rpc.sql`
4. `setup/migrations/004_roster_rpc.sql`
5. `setup/migrations/005_attendance_states.sql`

## Verificación

```sql
select code from public.course_offerings where code = 'TGA04-2026-2';
select count(*) from public.periods p
join public.course_offerings co on co.id = p.offering_id
where co.code = 'TGA04-2026-2';
-- Debe dar 15 semanas
```

## GitHub Pages

- Participación: https://dfdomin.github.io/tga04-neurobiz/dashboard/participacion.html
- Ahorcado: https://dfdomin.github.io/tga04-neurobiz/JuegoDelAhorcado/index.html

PIN docente: `sasadfgh2019`
