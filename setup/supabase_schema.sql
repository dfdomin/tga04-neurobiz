-- TGA04 · NeuroBiz S.A.S. · Supabase schema
-- Ejecutar una vez en Supabase SQL Editor.
-- No incluye DROP TABLE para evitar perdida accidental de datos.

create extension if not exists pgcrypto;

create table if not exists public.students (
  id uuid primary key default gen_random_uuid(),
  cc text unique not null,
  name text not null default '',
  grupo text not null default '',
  horario text not null default '',
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists public.student_progress (
  id uuid primary key default gen_random_uuid(),
  student_id text not null,
  student_name text not null default '',
  grupo text not null default '',
  horario text not null default '',
  semana int not null check (semana between 1 and 15),
  xp int not null default 0,
  quiz_score numeric not null default 0,
  quiz_answers jsonb not null default '{}'::jsonb,
  hti_done boolean not null default false,
  activity_done boolean not null default false,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  unique (student_id, semana)
);

create or replace function public.set_updated_at()
returns trigger language plpgsql as $$
begin
  new.updated_at = now();
  return new;
end;
$$;

drop trigger if exists trg_students_updated_at on public.students;
create trigger trg_students_updated_at
before update on public.students
for each row execute function public.set_updated_at();

drop trigger if exists trg_student_progress_updated_at on public.student_progress;
create trigger trg_student_progress_updated_at
before update on public.student_progress
for each row execute function public.set_updated_at();

create or replace view public.resumen_docente
  with (security_invoker = true)
as
select
  student_id,
  max(student_name) as student_name,
  max(grupo) as grupo,
  max(horario) as horario,
  count(distinct semana) as semanas_visitadas,
  sum(xp) as xp_total,
  avg(quiz_score) as quiz_promedio,
  sum(case when activity_done or hti_done then 1 else 0 end) as actividades,
  max(updated_at) as ultima_actualizacion
from public.student_progress
group by student_id;

alter table public.students enable row level security;
alter table public.student_progress enable row level security;

drop policy if exists "students_anon_select" on public.students;
create policy "students_anon_select" on public.students for select to anon using (true);

drop policy if exists "students_anon_insert" on public.students;
create policy "students_anon_insert" on public.students for insert to anon with check (true);

drop policy if exists "students_anon_update" on public.students;
create policy "students_anon_update" on public.students for update to anon using (true) with check (true);

drop policy if exists "progress_anon_select" on public.student_progress;
create policy "progress_anon_select" on public.student_progress for select to anon using (true);

drop policy if exists "progress_anon_insert" on public.student_progress;
create policy "progress_anon_insert" on public.student_progress for insert to anon with check (true);

drop policy if exists "progress_anon_update" on public.student_progress;
create policy "progress_anon_update" on public.student_progress for update to anon using (true) with check (true);

create table if not exists public.attendance (
  id uuid primary key default gen_random_uuid(),
  cc text not null,
  fecha date not null,
  estado text not null check (estado in ('P','T','F')),
  grupo text not null default '',
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  unique (cc, fecha)
);

alter table public.attendance enable row level security;

drop trigger if exists trg_attendance_updated_at on public.attendance;
create trigger trg_attendance_updated_at
before update on public.attendance
for each row execute function public.set_updated_at();

drop policy if exists "attendance_anon_select" on public.attendance;
create policy "attendance_anon_select" on public.attendance for select to anon using (true);

drop policy if exists "attendance_anon_insert" on public.attendance;
create policy "attendance_anon_insert" on public.attendance for insert to anon with check (true);

drop policy if exists "attendance_anon_update" on public.attendance;
create policy "attendance_anon_update" on public.attendance for update to anon using (true) with check (true);

grant usage on schema public to anon;
grant select, insert, update on public.students to anon;
grant select, insert, update on public.student_progress to anon;
grant select, insert, update on public.attendance to anon;
grant select on public.resumen_docente to anon;
