-- =============================================================================
-- Passage de la marque iCLAN a MIT et de la couleur d'accent au bleu.
--
-- A executer uniquement si l'evenement et les categories ont ete crees avant
-- ce changement. Sur un projet neuf, seed_games.sql contient deja les bonnes
-- valeurs.
-- =============================================================================

update events
set name = 'MIT Entrepreneur Challenge'
where name = 'iCLAN Entrepreneur Challenge';

update games
set color = '#2f80ed'
where slug = 'entrepreneuriat' and color = '#f4b93e';

alter table games
  alter column color set default '#2f80ed';
