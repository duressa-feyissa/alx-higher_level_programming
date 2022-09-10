-- Each record should display: tv_genres.name - rating sum
-- Results must be sorted in descending order by their rating

SELECT name, SUM(rate) AS rating
FROM tv_shows
JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres
ON tv_genres.id = genre_id
JOIN tv_show_ratings
ON tv_shows.id = tv_show_ratings.show_id
GROUP BY name
ORDER BY rating DESC;
