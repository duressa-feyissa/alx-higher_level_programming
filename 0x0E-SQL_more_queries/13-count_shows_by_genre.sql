-- Each record should display:
-- <TV Show genre> - <Number of shows linked to this genre>

SELECT name AS genre, COUNT(tv_show_genres.show_id)
FROM tv_genres
JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY name
ORDER BY COUNT(tv_show_genres.show_id) DESC;
