SELECT DISTINCT(name) FROM people JOIN stars ON id = person_id
WHERE person_id in (SELECT person_id from stars JOIN movies ON id = movie_id WHERE title = "Toy Story" ) ;

