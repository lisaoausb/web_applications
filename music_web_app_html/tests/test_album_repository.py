from lib.album_repository import *
from lib.album import *
"""
When we call AlbumRepository#all,
we get a list of all albums in seed database.
"""

def test_get_all_album_records(db_connection):
    db_connection.seed('seeds/music_library.sql')
    library = AlbumRepository(db_connection)

    albums = library.all() # get all albums

    assert len(albums) == 12

    assert albums[0].id == 1
    assert albums[0].title == 'Doolittle'
    assert albums[0].release_year == 1989
    assert albums[0].artist_id == 1

    assert albums[8].id == 9
    assert albums[8].title == 'Baltimore'
    assert albums[8].release_year == 1978
    assert albums[8].artist_id == 4

"""
we call AlbumRepository#find, 
and get a single album back
based on the number we specify
"""

def test_get_one_album(db_connection):
    db_connection.seed('seeds/music_library.sql')
    library = AlbumRepository(db_connection)
    album = library.find(3)
    assert str(album) == 'Album(3, Waterloo, 1974, 2)'

    # OR can also assert this way:

    assert album == Album(3, 'Waterloo', 1974, 2)

"""
When we call AlbumRepository#create,
we will create a new record in our database
based on the information we pass it (a new instance of album)
"""

def test_create(db_connection):
    library = AlbumRepository(db_connection)
    db_connection.seed('seeds/music_library.sql')
    new_album = Album(None, 'new album', 2023, 2)
    assert library.create(new_album) == None
    assert library.all() == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2),
        Album(5, 'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Baltimore', 1978, 4),
        Album(10, 'Here Comes the Sun', 1971, 4),
        Album(11, 'Fodder on My Wings', 1982, 4),
        Album(12, 'Ring Ring', 1973, 2),
        Album(13, 'new album', 2023, 2)
        ]

"""
When we all AlbumRepository#delete,
we will delete an existing record from our database,
based on the id number we give it
"""

def test_delete(db_connection):
    db_connection.seed('seeds/music_library.sql')
    library = AlbumRepository(db_connection)
    assert library.delete(10) == None
    assert library.all() == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2),
        Album(5, 'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Baltimore', 1978, 4),
        Album(11, 'Fodder on My Wings', 1982, 4),
        Album(12, 'Ring Ring', 1973, 2),
        ]
    
    