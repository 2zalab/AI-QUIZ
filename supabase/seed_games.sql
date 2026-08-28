-- =============================================================================
-- Donnees de base : l'evenement et les quatre categories de jeu.
-- A executer APRES schema.sql et AVANT l'import des questions.
-- =============================================================================

insert into events (name, description, status)
select 'iCLAN Entrepreneur Challenge', 'Business, innovation et culture camerounaise', 'open'
where not exists (select 1 from events);

insert into games (event_id, slug, name, description, emoji, color, questions_per_session)
values
  ((select id from events order by created_at limit 1), 'entrepreneuriat', 'Entrepreneuriat',
   'Business, marketing, financement, gestion et innovation.', '💼', '#f4b93e', 10),
  ((select id from events order by created_at limit 1), 'cameroun', 'Cameroun',
   'Culture, histoire, geographie, economie et personnalites.', '🇨🇲', '#22c8b0', 10),
  ((select id from events order by created_at limit 1), 'innovation-ia', 'Innovation & IA',
   'Le numerique et l''intelligence artificielle au quotidien.', '💡', '#8b7cf6', 10),
  ((select id from events order by created_at limit 1), 'mixte', 'Challenge Mixte',
   'Un melange des trois univers, pour les plus polyvalents.', '🎯', '#f472b6', 10)
on conflict (slug) do update
set name        = excluded.name,
    description = excluded.description,
    emoji       = excluded.emoji,
    color       = excluded.color;
