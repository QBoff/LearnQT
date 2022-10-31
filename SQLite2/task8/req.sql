DELETE FROM films
WHERE genre = (
    SELECT id FROM genres WHERE title = 'фантастика'
) AND year < 2000 AND duration > 90