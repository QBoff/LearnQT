SELECT DISTINCT
  artist.name
FROM 
  track
LEFT JOIN genre ON track.genreid = genre.genreid
LEFT JOIN album ON track.albumid = album.albumid
LEFT JOIN artist ON album.artistid = artist.artistid
WHERE genre.name = ?
ORDER BY artist.name;