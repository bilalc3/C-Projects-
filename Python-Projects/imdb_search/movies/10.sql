
SELECT DISTINCT(name) from people JOIN directors ON id=person_id in (SELECT person_id from directors JOIN movies ON id = movie_id where movie_id in ((SELECT movie_id from ratings where rating>=9.0)));


