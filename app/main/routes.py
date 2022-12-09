from app.main import bp
from flask import Flask, redirect, render_template,request, url_for, flash
from app.models.message import Message
from flask_login import login_required, current_user



@bp.route('/')
def index():
    messages = Message.query.all()
    return render_template('index.html', messages = messages )
    

@bp.app_errorhandler(404)
def page_not_found(error):
    print(error)
    return render_template('page_not_found.html'), 404