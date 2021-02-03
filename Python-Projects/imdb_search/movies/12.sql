SELECT title from movies JOIN stars ON id = movie_id
where person_id = (SELECT id from people where name = "Helena Bonham Carter")
AND id in (SELECT movie_id from stars where person_id = (SELECT id from people where name = "Johnny Depp"));
