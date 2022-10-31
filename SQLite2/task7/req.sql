UPDATE films
SET duration = 100
WHERE genre = (
    SELECT id FROM genres WHERE title = 'мюзикл'
) AND duration > 100