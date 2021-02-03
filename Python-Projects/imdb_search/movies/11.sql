SELECT title from movies WHERE id in (
SELECT movie_id from ratings WHERE movie_id in 
(SELECT movie_id from stars JOIN people ON id = person_id where person_id in
(SELECT id from people WHERE name ="Chadwick Boseman")) ORDER BY rating DESC LIMIT 5); 


