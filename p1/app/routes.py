from app import app
from flask import Flask, render_template, redirect
from app.forms import LoginForm


@app.route('/login', methods=['GET', 'POST'])
def loin():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login request for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data
        ))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
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