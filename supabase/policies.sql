-- =============================================================================
-- Politiques de securite (RLS) - MIT Entrepreneur Challenge
--
-- Principe : le navigateur ne peut LIRE que le strict necessaire au classement
-- (nom, score, statut). Les questions, les bonnes reponses et les reponses des
-- joueurs restent inaccessibles depuis le client. Toutes les ecritures passent
-- par les routes API du serveur, qui utilisent la cle de service.
-- =============================================================================

alter table events           enable row level security;
alter table games            enable row level security;
alter table questions        enable row level security;
alter table players          enable row level security;
alter table player_questions enable row level security;
alter table answers          enable row level security;

-- --- Lecture publique : evenements et categories -----------------------------
drop policy if exists "events lisibles" on events;
create policy "events lisibles" on events for select to anon, authenticated using (true);

drop policy if exists "games lisibles" on games;
create policy "games lisibles" on games for select to anon, authenticated using (true);

-- --- Lecture publique : joueurs (classement en direct) -----------------------
-- Aucune colonne sensible n'existe dans cette table : seuls le nom, le score et
-- le statut y figurent. C'est ce qui permet au temps reel d'alimenter /display.
drop policy if exists "classement lisible" on players;
create policy "classement lisible" on players for select to anon, authenticated using (true);

-- --- Aucune ecriture cote client ---------------------------------------------
-- Volontairement : pas de policy insert/update/delete pour anon. Un joueur ne
-- peut donc pas modifier son score depuis la console du navigateur.

-- --- Tables totalement fermees au client -------------------------------------
-- questions, player_questions et answers n'ont AUCUNE policy pour anon :
-- avec RLS active, cela signifie qu'aucune ligne n'est lisible ni modifiable.
-- Seule la cle de service (utilisee uniquement cote serveur) les atteint.

-- Revocation explicite des droits de table pour les roles publics.
revoke all on questions        from anon, authenticated;
revoke all on player_questions from anon, authenticated;
revoke all on answers          from anon, authenticated;

grant select on leaderboard to anon, authenticated;
