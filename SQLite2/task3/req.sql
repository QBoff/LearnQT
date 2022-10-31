UPDATE films
SET duration = duration * 2
WHERE genre = (
    SELECT id FROM genres
    WHERE title = "фантастика"
)
