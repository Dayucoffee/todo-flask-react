from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required
from core import app, db

@app.route('/')
def index():
    greeting= "Howdy!"
    return render_template('index.html', greet=greeting)

