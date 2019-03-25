from . import auth
from flask import render_template, flash, redirect, url_for, session
from flask_login import current_user
from ...form import LoginForm, RegisterForm
#from ...models import Todo
#from ... import db


@auth.route('/login')
def login():
    form = LoginForm()
    return render_template('auth/login.html', form=form)

@auth.route('/register')
def register():
    return render_template('auth/register.html')

@auth.route('/logout')
def logout():
    return 'logout'

