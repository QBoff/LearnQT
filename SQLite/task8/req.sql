SELECT DISTINCT title FROM genres
WHERE id IN (
    SELECT genre FROM films WHERE year = 2010 OR year = 2011
)