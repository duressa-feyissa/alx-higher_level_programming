-- list all genres not linked to the show Dexter

SELECT name FROM tv_genres
WHERE name NOT IN
(SELECT DISTINCT name FROM tv_genres
JOIN tv_show_genres
ON tv_genres.id = genre_id
JOIN tv_shows
ON tv_shows.id = show_id
WHERE title = "Dexter")
ORDER BY name;
