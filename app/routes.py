from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm

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
    

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title = 'Sign In', form = form)

