-- The tv_shows table contains only one record where title = Dexter

SELECT name
FROM tv_genres
JOIN tv_show_genres
JOIN tv_shows
ON tv_genres.id = genre_id and tv_shows.id = show_id
WHERE title = "Dexter"
ORDER BY name;
