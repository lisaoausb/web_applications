import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist_repository import ArtistRepository
from lib.artist import Artist

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route('/albums', methods=['POST'])
def add_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    if 'title' and 'release_year' and 'artist_id' not in request.form:
        return 'Invalid - You need to add an album', 400
    album1 = Album(None, request.form['title'], request.form['release_year'],request.form['artist_id'])
    repository.create(album1)
    return ''

@app.route('/albums')
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    # return "\n".join([album.title for album in albums])
    return render_template('album/index.html', albums=albums)

@app.route('/albums/<id>')
def get_one_album(id):
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)
    artist_repository = ArtistRepository(connection)
    album = album_repository.find(id)
    artist = artist_repository.find(album.artist_id)
    return render_template('album/album.html', album=album, artist=artist)

@app.route('/artists', methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all()
    return ", ".join(f"{artist.name}" for artist in artists)

@app.route('/artists', methods=['POST'])
def post_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    new_artist = Artist(None, request.form['name'], request.form['genre'])
    repository.create(new_artist)
    return '', 200

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://localhost:5000/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return render_template('emoji.html', emoji=':)')

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

