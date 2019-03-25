from . import teste
from flask import render_template, flash, redirect, url_for, session
from flask_login import current_user
#from ...form import TodoForm
#from ...models import Todo
#from ... import db


@teste.route('/', methods=['GET', 'POST'])
def index():
    return render_template('home/index.html')