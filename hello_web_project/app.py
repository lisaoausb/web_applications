import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route('/sort_names', methods=['POST'])
def sort_names():
    if 'names' not in request.form:
        return 'Please provide names', 400
    names = request.form['names'].split(',')
    names.sort()
    print(names)
    return ','.join(names)

@app.route('/count_vowels', methods=['POST'])
def count_vowels():
    text = request.form['text']
    count = 0
    for letter in text:
        if letter in 'aeiou':
            count += 1
    return f'There are {count} vowels in "{text}"'

@app.route('/names', methods=['GET'])
def add_name():
    names = ['Julia', 'Alice', 'Karim']
    if not request.args:
        return ', '.join(names)
    else:
        new_names = request.args['add'].split(',')
        for name in new_names:
            names.append(name)
        return ', '.join(sorted(names))

# POST /submit
# With body parameters:
# name=Leo
# message=Hello world
# Expected response: (200 OK):
# Thanks Leo, you sent this message: "Hello world"
# ; curl -X POST -d "name=Lisa&message="Hello,%20world"" http://localhost:5000/submit

@app.route('/submit', methods=['POST'])
def post_message():
    name = request.form['name']
    message = request.form['message']
    return f'Thanks, {name}, you sent this message: "{message}".'
# GET /wave
# Parameter: name
# name=Lisa
# Expected response: (200 OK):
# I am waing at (name)
# curl -X GET http://localhost:5000/wave\?name\=Lisa

@app.route('/wave', methods=['GET'])
def wave():
    name = request.args['name']
    return f'I am waving at {name}'



# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://localhost:5000/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

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

