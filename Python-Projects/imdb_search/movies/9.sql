SELECT DISTINCT(name) from people
JOIN stars on id = person_id
WHERE person_id in
(SELECT person_id from stars join movies on id = movie_id where id in
(SELECT id from movies where year = 2004)) ORDER BY birth;