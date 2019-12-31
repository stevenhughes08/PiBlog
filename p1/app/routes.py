from app import app
from flask import Flask, render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Steven'}
    posts = [
        {
            'author': {'username': 'Svengali'},
            'body': 'I am the anti-clown.'
        },
        {
            'author': {'username': 'Bubble-ishus'},
            'body': 'Ba boo, ba ba boo!'

        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)