# Migrations

Scripts a executer **uniquement si vous avez deja lance `schema.sql` dans une
version anterieure**. Sur un projet Supabase neuf, `schema.sql` contient deja
l'etat final : ces fichiers sont alors inutiles.

| Fichier | A executer si... |
| --- | --- |
| `001_questions_per_session_sans_plafond.sql` | vous avez cree la table `games` avec la contrainte `between 3 and 50` |
