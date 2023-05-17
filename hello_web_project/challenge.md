03_CHALLENGE Route Design Recipe

Copy this design recipe template to test-drive a plain-text Flask route.

1. Design the Route Signature

Include the HTTP method, the path, and any query or body parameters.


# Request: Home route
GET http://127.0.0.1:5000/names?add=Eddie

# Expected response (sorted list of names):
Julia, ALice, Karim, Eddie


2. Create Examples as Tests

Go through each route and write down one or more example responses.

Remember to try out different parameter values.

Include the status code and the response body.

# GET /names
# Parameters: none
# Expected response (200 OK)
"""
Julia, Alice, Karim
"""

# GET /names
# Parameters:
#   add: Eddie
# Expected response: 200 OK
"""
Julia, Alice, Karim, Eddie
"""


3. Test-drive the Route

After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

Here's an example for you to start with:


"""
GET /names
Parameters: none
Expected response (200 OK)
Julia, Alice, Karim
"""

def test_existing_names(web_client):
    response = web_client.get('/names')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Julia, Alice, Karim'

"""
GET /names
Parameters:
  add: Eddie
Expected response: 200 OK
Julia, Alice, Karim, Eddie
"""
def test_add_name(web_client):
    response = web_client.get('/names?add=Eddie')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Julia, Alice, Karim, Eddie'