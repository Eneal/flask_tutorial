from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Ezra'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    template_replacements = {
        'title': 'Home',
        'user': user,
        'posts': posts
    }
    return render_template('index.html', **template_replacements)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for {form.username.data}, remember_me={form.remember_me.data}')
        return redirect(url_for('index'))
    template_replacements = {
        'title': 'Sign In',
        'form': form
    }
    return render_template('login.html', **template_replacements)
