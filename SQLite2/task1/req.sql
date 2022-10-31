DELETE FROM films
WHERE films.genre = (
    SELECT genres.id FROM genres WHERE genres.title = "комедия"
)