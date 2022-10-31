DELETE FROM films
WHERE duration >= 90 AND genre = (
    SELECT id FROM genres
    WHERE title = "боевик"
)