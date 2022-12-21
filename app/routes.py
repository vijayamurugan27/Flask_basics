from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'vijay'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': "we have succesfully created  a new post"
        },
        {
            'author': {'username': 'Mary'},
            'body': "This is my second post."
        }
    ]
    return render_template('index.html', title = 'home', user = user, posts = posts) 
    