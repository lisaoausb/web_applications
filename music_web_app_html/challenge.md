_03_challenge Route Design Recipe

Copy this design recipe template to test-drive a plain-text Flask route.

1. Design the Route Signature

Include the HTTP method, the path, and any query or body parameters.

1. Add a route GET /artists/<id> which returns an HTML page showing details for a single artist.
2. Add a route GET /artists which returns an HTML page with the list of artists. This page should contain a link for each artist listed, linking to /artists/<id> where <id> needs to be the corresponding artist id.

Single artist route
GET artists/<id>

All artist route
GET artists

2. Create Examples as Tests

Go through each route and write down one or more example responses.

Remember to try out different parameter values.

Include the status code and the response body.

"""
GET /artists
Expected response: 200 OK
expect all artists in database
"""

"""GET /artists/<id>
Expected response 200 OK
expect artist specified in id
"""

3. Test-drive the Route

After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

Here's an example for you to start with:

"""
GET /home
  Expected response (200 OK):
  "This is my home page!"
"""
def test_get_home(web_client):
    response = web_client.get('/home')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'This is my home page!'

"""
POST /submit
  Parameters:
    name: Leo
    message: Hello world
  Expected response (200 OK):
  "Thanks Leo, you sent this message: "Hello world""
"""
def test_post_submit(web_client):
    response = web_client.post('/submit', data={'name': 'Leo', 'message': 'Hello world'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Thanks Leo, you sent this message: "Hello world"'
