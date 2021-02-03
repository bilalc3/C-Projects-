SELECT DISTINCT(name) from people where id in
(SELECT person_id from stars where movie_id in
(SELECT movie_id from stars JOIN people ON id =person_id where person_id = (SELECT id from people where name = "Kevin Bacon")
AND birth = 1958 ));