-- The tv_genres table contains only one record where name = Comedy

SELECT title
FROM tv_genres
JOIN tv_show_genres
JOIN tv_shows
ON tv_genres.id = genre_id and tv_shows.id = show_id
WHERE name = "Comedy"
ORDER BY title;
