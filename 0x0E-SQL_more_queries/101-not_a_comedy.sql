-- The tv_genres table contains only one record
-- where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title

SELECT title FROM tv_shows
WHERE title NOT IN
(SELECT title FROM tv_shows
JOIN tv_show_genres
ON tv_shows.id = show_id
JOIN tv_genres
ON tv_genres.id = genre_id
WHERE name = "Comedy")
ORDER BY title;
