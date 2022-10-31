SELECT DISTINCT album.title

FROM track

LEFT JOIN genre ON track.genreid = genre.genreid
LEFT JOIN album ON track.albumid = album.albumid
LEFT JOIN artist ON artist.artistid = album.artistid
WHERE genre.name = '?'
ORDER BY artist.artistid, album.title;