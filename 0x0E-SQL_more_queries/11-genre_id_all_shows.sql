-- A script that lists all the shows contained in the database
-- hbtn_0d_tvshows
-- Eech record should display: tv_shows.title - tv_show_genres.genre_id
-- IF a show doesnt have a genre, display NULL
SELECT tv_shows.title,tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id=tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
