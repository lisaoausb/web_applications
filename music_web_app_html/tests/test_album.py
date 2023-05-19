from lib.album import Album

def test_album_contructs():
    album = Album(1, 'This is Why', 2023, 6)
    assert album.id == 1
    assert album.title == 'This is Why'
    assert album.release_year == 2023
    assert album.artist_id == 6

def test_albums_are_equal():
    album1 = Album(1, 'This is Why', 2023, 6) 
    album2 = Album(1, 'This is Why', 2023, 6)
    assert album1 == album2

def test_formats_nicely():
    album = Album(1, 'This is Why', 2023, 6)
    assert str(album) == "Album(1, This is Why, 2023, 6)"