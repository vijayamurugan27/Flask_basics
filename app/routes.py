from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    # return "<h1> Hello, World! </h1>"
    user = {'username': 'Miguel'}
    return '''
    <html>
        <head>
            <title>Home Page - Microblog</title>
        </head>
        <body>
            <h1>Hello, ''' + user['username'] + '''!</h1>
        </body>
    </html>'''
