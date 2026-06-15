-- TGA04 · Preservar tablas legacy antes del esquema unificado
-- Ejecutar PRIMERO en Supabase SQL Editor (nnrgxuzvjtweyzkdrech).
-- No elimina filas: solo renombra tablas si existen con el esquema antiguo TGA04.

do $$
begin
  if exists (
    select 1 from information_schema.columns
    where table_schema = 'public'
      and table_name = 'student_progress'
      and column_name = 'progress'
  ) and not exists (
    select 1 from information_schema.tables
    where table_schema = 'public' and table_name = 'tga04_student_progress_legacy'
  ) then
    alter table public.student_progress rename to tga04_student_progress_legacy;
    comment on table public.tga04_student_progress_legacy is
      'Respaldo TGA04 pre-unificación (progress jsonb sin student_id).';
  end if;

  if exists (
    select 1 from information_schema.columns
    where table_schema = 'public'
      and table_name = 'quiz_scores'
      and column_name = 'week'
  ) and not exists (
    select 1 from information_schema.tables
    where table_schema = 'public' and table_name = 'tga04_quiz_scores_legacy'
  ) then
    alter table public.quiz_scores rename to tga04_quiz_scores_legacy;
    comment on table public.tga04_quiz_scores_legacy is
      'Respaldo TGA04 pre-unificación (quiz_scores sin student_id).';
  end if;

  if exists (
    select 1 from information_schema.tables
    where table_schema = 'public' and table_name = 'student_participation'
  ) and not exists (
    select 1 from information_schema.tables
    where table_schema = 'public' and table_name = 'tga04_student_participation_legacy'
  ) then
    alter table public.student_participation rename to tga04_student_participation_legacy;
    comment on table public.tga04_student_participation_legacy is
      'Respaldo TGA04 pre-unificación (participación jsonb).';
  end if;
end;
$$;
