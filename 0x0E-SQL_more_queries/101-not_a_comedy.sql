-- A script that lists all shows without the genre comedy in the database hbtn_0d_tvshows
-- The tv_genres table contains only one record where name = comedy (but the id can be different)
-- Each record should display tv_shows.title 
-- Results must be sorted in ascending order by the show title
-- You can use a maximum of two select statements 

SELECT tv_shows.title FROM tv_shows
WHERE tv_shows.id NOT IN
(SELECT tv_shows.id
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = "Comedy")
ORDER BY tv_shows.title;
