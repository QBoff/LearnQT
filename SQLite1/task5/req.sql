SELECT DISTINCT Name FROM Track
    WHERE AlbumId IN (
        SELECT AlbumId FROM Album
            WHERE ArtistId IN (
                SELECT ArtistId FROM Artist
                    WHERE name = "?"))
    ORDER BY Name