{{ NAME }} Route Design Recipe

Copy this design recipe template to test-drive a plain-text Flask route.

1. Design the Route Signature

Include the HTTP method, the path, and any query or body parameters.


# Request: Home route
POST http://127.0.0.1:5000/sort-names

# With body parameters:
names=Joe,Alice,Zoe,Julia,Kieran

# Expected response (sorted list of names):
Alice,Joe,Julia,Kieran,Zoe

# Sort names route
POST /sort-names
    names: string (or list?)

2. Create Examples as Tests

Go through each route and write down one or more example responses.

Remember to try out different parameter values.

Include the status code and the response body.

# POST /sort-names
# Parameters: none
# Expected response (400 Bad request)
"""
Please provide a name and a message
"""

# POST /sort-names
# Parameters:
#   names: Joe, Alice, Zoe, Julia, Kieren
# Expected response: 200 OK
"""
Alice,Joe,Julia,Kieran,Zoe
"""


3. Test-drive the Route

After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

Here's an example for you to start with:


"""
POST /sort-names
Parameters: none
Expected response (400 Bad request)
Please provide a name and a message
"""
def test_post_sort_names_none(web_client):
    response = web_client.post('/sort_names')
    assert response.status_code == 400
    assert response.data.decode('utf-8') == 'Please provide a name and a message'

"""å
POST /sort-names
Parameters:
  names: Joe, Alice, Zoe, Julia, Kieren
Expected response: 200 OK
Alice,Joe,Julia,Kieran,Zoe
"""
def test_post_sort_names(web_client):
    response = web_client.post('/sort_names', data={'name': 'Joe,Alice,Zoe,Julia,Kieran'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice,Joe,Julia,Kieran,Zoe'

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
