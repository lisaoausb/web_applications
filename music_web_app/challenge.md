04 CHALLENGE Route Design Recipe

1. Design the Route Signature

# Artist route
GET /artists

POST /artists
    name: string
    genre: string

2. Create Examples as Tests

Go through each route and write down one or more example responses.

Remember to try out different parameter values.

Include the status code and the response body.

# Request:
GET /artists

# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone

# Request:
POST /artists

# With body parameters:
name=Wild nothing
genre=Indie

# Expected response (200 OK)
(No content)

# Then subsequent request:
GET /artists

# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing

3. Test-drive the Route

Here's an example for you to start with:

"""
GET /artists
  Expected response (200 OK):
    Pixies, ABBA, Taylor Swift, Nina Simone
"""
def test_get_artists(web_client):
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Pixies, ABBA, Taylor Swift, Nina Simone'

"""
POST /artists
  Parameters:
    name: Wild nothing
    genre: Indie
  Expected response (200 OK):
  (No content)
"""
def test_post_artist(web_client):
    response = web_client.post('/artists', data={'name': 'Wild nothing', 'genre': 'Indie'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == ''


"""
GET /artists after using POST
    Expected response: 200(OK)
    'Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing'
"""

def test_get_artists_after_post(web_client):
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing'

