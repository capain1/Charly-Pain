# 4.1 To update the seats:
UPDATE showings
SET available_seats = 0
WHERE movie_ID = 2 AND start_time >= '17:00:00';
# Nothing is displayed

# 4.2  to display all PG and U films
SELECT *
FROM movie_info
WHERE age_rating IN ('PG', 'U');
## the 3D amaxing movie, The Cartoon, The scary Cartoon

#4.3 to show all films that are not in a 4K screen
SELECT DISTINCT movie_name
FROM movie_info
INNER JOIN showings ON movie_info.movie_ID = showings.movie_ID
INNER JOIN screens ON showings.screen_ID = screens.screen_ID
WHERE screens.four_k = False;
# The Movie

# 4.4  Start time of film with highest number of seats available 
SELECT movie_info.movie_name, showings.start_time
FROM showings
INNER JOIN movie_info ON showings.movie_ID = movie_info.movie_ID
WHERE showings.available_seats = (
    SELECT (available_seats)
    FROM showings)
# Cannot get this code to work. I have selected movies from showings and start times, I have then used inner join to join then based on the movie ID, and Where is supposed to show only those with the highest number of seats?

#4.5 
SELECT m.name AS movie_name, s.start_time, ADDTIME(s.start_time, CONCAT(m.length, ':00')) AS end_time
FROM movies AS m
JOIN screenings AS s ON m.movie_id = s.movie_id

#I cannot get this code to work either, 