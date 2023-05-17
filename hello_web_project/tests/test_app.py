# Tests for your routes go here
# File: tests/test_app.py

"""
When: I make a POST request to /count_vowels
And: I send "eee" as the body parameter text
Then: I should get a 200 response with 3 in the message
"""
def test_post_count_vowels_eee(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eee'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 3 vowels in "eee"'

"""
When: I make a POST request to /count_vowels
And: I send "eunoia" as the body parameter text
Then: I should get a 200 response with 5 in the message
"""
def test_post_count_vowels_eunoia(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eunoia'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 5 vowels in "eunoia"'

"""
When: I make a POST request to /count_vowels
And: I send "mercurial" as the body parameter text
Then: I should get a 200 response with 4 in the message
"""
def test_post_count_vowels_mercurial(web_client):
    response = web_client.post('/count_vowels', data={'text': 'mercurial'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 4 vowels in "mercurial"'

"""
# POST /sort-names
# Parameters: none
# Expected response (400 Bad request)
# Please provide a name and a message
# """
def test_post_sort_names_none(web_client):
    response = web_client.post('/sort_names')
    assert response.status_code == 400
    assert response.data.decode('utf-8') == 'Please provide names'

"""
POST /sort-names
Parameters:
    names: Joe, Alice, Zoe, Julia, Kieren
Expected response: 200 OK
Alice,Joe,Julia,Kieran,Zoe
"""
def test_post_sort_names(web_client):
    response = web_client.post('/sort_names', data={'names': 'Joe,Alice,Zoe,Julia,Kieran,Ana'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice,Ana,Joe,Julia,Kieran,Zoe'

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
    assert response.data.decode('utf-8') == 'Alice, Eddie, Julia, Karim'

def test_add_multiple_names_and_sort(web_client):
    response = web_client.get('/names?add=Eddie,Leo')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice, Eddie, Julia, Karim, Leo'
    

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

# === End Example Code ===
