from flask_login import login_required 
from flask import render_template,redirect,url_for,abort
from . import main
from ..models import User
from flask_login import login_required, current_user






# Views

@main.route('/')
def index():


    title = 'Home - pitchesssss '

    return render_template('index.html', title = title)


