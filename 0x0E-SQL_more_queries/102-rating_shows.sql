-- Each record should display: tv_shows.title - rating sum
-- Results must be sorted in descending order by the rating

SELECT title, SUM(rate) AS rating
FROM tv_shows
JOIN tv_show_ratings
ON tv_shows.id = show_id
GROUP BY title
ORDER BY rating DESC;
