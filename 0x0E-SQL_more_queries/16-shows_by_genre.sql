-- If a show doesn’t have a genre, display NULL in the genre column
-- Each record should display: tv_shows.title - tv_genres.name
-- Results must be sorted in ascending order by the show title and genre name

SELECT title, name
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = show_id
LEFT JOIN tv_genres
ON tv_genres.id = genre_id
ORDER BY title, name;
