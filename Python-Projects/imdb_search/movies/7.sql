SELECT title,rating
FROM ratings JOIN movies ON movie_id = id
WHERE year=2010
ORDER BY rating DESC, title;