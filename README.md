# TGA04 · NeuroBiz

Material gamificado para **Fundamentos de Computación para los Negocios**.

## Entradas principales

- `index.html`: landing para GitHub Pages.
- `semanaN/index.html`: material del estudiante.
- `semanaN/notas_profesor.html`: guía docente.
- `dashboard/index.html`: progreso local del estudiante.
- `dashboard/profesor.html`: panel docente con Supabase.
- `dashboard/notas.html`: consolidador de notas.
- `dashboard/participacion.html`: participación en clase + asistencia (P/T/F) + exportación CSV.
- `setup/CONFIGURAR_SUPABASE.html`: guía de configuración.
- `setup/supabase_schema.sql`: esquema de base de datos.
- `setup/backup.py` / `setup/restore.py`: respaldo y restauración de Supabase con migración automática.
- `setup/exportar_notas.py`: exportación de notas a CSV desde Supabase.
- `setup/smoke_test.py`: verificación de links rotos en todos los HTML.

## Publicación

Publicar como sitio estático en GitHub Pages y usar recursos tipo URL en Moodle.
Antes de usar dashboards cloud, configurar `js/supabase-config.js` y ejecutar el SQL de `setup/supabase_schema.sql`.

## Documentación

Documentación completa del proyecto siguiendo **BDD + TDD + SDD (IEEE 1016)**:

- [`docs/SDD.md`](docs/SDD.md) — Software Design Description (arquitectura, modelo de datos, interfaces)
- [`docs/BDD/`](docs/BDD/) — Behavior-Driven Development (36 escenarios Gherkin en 5 features)
- [`docs/TDD/`](docs/TDD/) — Test-Driven Development (50+ casos de prueba, Red-Green-Refactor)

## Verificación

```bash
python3 setup/smoke_test.py          # Revisa links rotos (34 HTMLs)
python3 -m py_compile setup/*.py     # Valida sintaxis Python (4 scripts)
```
