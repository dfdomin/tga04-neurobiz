# Configuración Supabase — TGA04 (NeuroBiz)

**Proyecto compartido IUB** (mismo que ADM18):  
`https://nnrgxuzvjtweyzkdrech.supabase.co` · ref `nnrgxuzvjtweyzkdrech`  
Offering: `TGA04-2026-2`

Ver `setup/IUB_SUPABASE_COMPARTIDO.md` para credenciales y comandos CLI.

## Scripts SQL (solo si falta algo en el proyecto remoto)

Los datos ya viven en el Supabase unificado. Ejecutar solo si verificas que falta:

1. `setup/gamification_unified.sql`
2. `setup/migrations/003_tga04_seed_and_rpc.sql` (en este repo, semanas TGA04)
3. Migraciones ADM18 compartidas: `004_*`, `005_*`, `006_*`

## Verificación

```sql
select code from public.course_offerings where code = 'TGA04-2026-2';
select count(*) from public.periods p
join public.course_offerings co on co.id = p.offering_id
where co.code = 'TGA04-2026-2';
```

## GitHub Pages

- Participación: https://dfdomin.github.io/tga04-neurobiz/dashboard/participacion.html
- Ahorcado: https://dfdomin.github.io/tga04-neurobiz/JuegoDelAhorcado/index.html

PIN docente: `sasadfgh2019`
