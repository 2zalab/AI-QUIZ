-- =============================================================================
-- Retire le plafond arbitraire de 50 questions par partie.
--
-- La borne haute n'a plus de raison d'etre en base : le nombre de questions
-- servies est de toute facon limite a l'execution par la taille de la banque de
-- la categorie. Seule reste la garantie qu'une partie compte au moins une
-- question.
--
-- A n'executer que si la table games a ete creee avec l'ancienne contrainte.
-- =============================================================================

alter table games
  drop constraint if exists games_questions_per_session_check;

alter table games
  alter column questions_per_session type integer;

alter table games
  add constraint games_questions_per_session_check
  check (questions_per_session > 0);
