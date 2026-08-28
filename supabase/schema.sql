-- =============================================================================
-- iCLAN Entrepreneur Challenge - schema Supabase / PostgreSQL
-- A executer dans l'editeur SQL de Supabase (ou via `supabase db push`).
-- =============================================================================

create extension if not exists "pgcrypto";

-- --- Types -------------------------------------------------------------------
do $$ begin
  create type difficulty_level as enum ('facile', 'moyen', 'challenge');
exception when duplicate_object then null; end $$;

do $$ begin
  create type player_status as enum ('waiting', 'playing', 'finished');
exception when duplicate_object then null; end $$;

-- --- Evenement ---------------------------------------------------------------
create table if not exists events (
  id            uuid primary key default gen_random_uuid(),
  name          text        not null,
  description   text        not null default '',
  status        text        not null default 'open' check (status in ('draft', 'open', 'closed')),
  start_at      timestamptz,
  end_at        timestamptz,
  created_at    timestamptz not null default now()
);

-- --- Categories de jeu -------------------------------------------------------
create table if not exists games (
  id                    uuid primary key default gen_random_uuid(),
  event_id              uuid references events (id) on delete cascade,
  slug                  text        not null unique,
  name                  text        not null,
  description           text        not null default '',
  emoji                 text        not null default '',
  color                 text        not null default '#f4b93e',
  -- Pas de plafond arbitraire : le nombre de questions par partie est borne a
  -- l'execution par la taille de la banque de la categorie.
  questions_per_session integer     not null default 10 check (questions_per_session > 0),
  is_active             boolean     not null default true,
  created_at            timestamptz not null default now()
);

-- --- Questions ---------------------------------------------------------------
-- La colonne correct_answer ne doit jamais etre exposee au navigateur :
-- les politiques RLS plus bas interdisent toute lecture anonyme de cette table.
create table if not exists questions (
  id             text primary key,
  game_id        uuid             not null references games (id) on delete cascade,
  difficulty     difficulty_level not null,
  question       text             not null,
  option_a       text             not null,
  option_b       text             not null,
  option_c       text             not null,
  option_d       text             not null,
  correct_answer char(1)          not null check (correct_answer in ('A', 'B', 'C', 'D')),
  points         smallint         not null default 100,
  time_limit     smallint         not null default 20 check (time_limit between 5 and 300),
  explanation    text             not null default '',
  tags           text             not null default '',
  created_at     timestamptz      not null default now()
);

create index if not exists questions_game_difficulty_idx on questions (game_id, difficulty);

-- --- Joueurs -----------------------------------------------------------------
create table if not exists players (
  id            uuid primary key default gen_random_uuid(),
  event_id      uuid references events (id) on delete cascade,
  game_id       uuid          not null references games (id) on delete cascade,
  name          text          not null check (char_length(trim(name)) between 1 and 24),
  session_code  text          not null unique,
  score         integer       not null default 0 check (score >= 0),
  correct_count smallint      not null default 0,
  answered_count smallint     not null default 0,
  status        player_status not null default 'waiting',
  started_at    timestamptz   not null default now(),
  finished_at   timestamptz,
  created_at    timestamptz   not null default now()
);

create index if not exists players_score_idx on players (score desc, started_at asc);
create index if not exists players_game_idx on players (game_id);

-- --- Questions tirees pour une partie ----------------------------------------
create table if not exists player_questions (
  id           uuid primary key default gen_random_uuid(),
  player_id    uuid     not null references players (id) on delete cascade,
  question_id  text     not null references questions (id) on delete cascade,
  order_number smallint not null,
  served_at    timestamptz,
  answered     boolean  not null default false,
  unique (player_id, order_number)
);

create index if not exists player_questions_player_idx on player_questions (player_id, order_number);

-- --- Reponses ----------------------------------------------------------------
create table if not exists answers (
  id           uuid primary key default gen_random_uuid(),
  player_id    uuid    not null references players (id) on delete cascade,
  question_id  text    not null references questions (id) on delete cascade,
  answer       char(1) check (answer in ('A', 'B', 'C', 'D')),
  is_correct   boolean not null default false,
  points       integer not null default 0,
  speed_bonus  integer not null default 0,
  time_taken_ms integer,
  answered_at  timestamptz not null default now(),
  unique (player_id, question_id)
);

create index if not exists answers_player_idx on answers (player_id);

-- --- Vue de classement -------------------------------------------------------
-- Vue publique : elle n'expose que ce qui doit s'afficher sur l'ecran geant.
create or replace view leaderboard as
select
  p.id,
  p.name,
  g.slug as game_slug,
  g.name as game_name,
  p.score,
  p.status,
  p.correct_count,
  p.answered_count,
  p.started_at,
  rank() over (order by p.score desc, p.started_at asc) as rank
from players p
join games g on g.id = p.game_id;

-- --- Diffusion temps reel ----------------------------------------------------
-- Active la replication temps reel sur la table des joueurs : c'est elle qui
-- alimente le classement en direct de l'ecran public.
do $$
begin
  if not exists (
    select 1 from pg_publication_tables
    where pubname = 'supabase_realtime' and tablename = 'players'
  ) then
    alter publication supabase_realtime add table players;
  end if;
end $$;
