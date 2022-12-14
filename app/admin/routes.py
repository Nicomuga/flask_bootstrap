from app.admin import bp
from flask import Flask, redirect, render_template,request, url_for, flash
from app.models.message import Message
from flask_login import login_required, current_user



@bp.route('/')
@login_required
def index():
    id = current_user.id
    if id == 1:
        return render_template('admin/index.html')
    else:
        flash('Lo siento, solo el admin puede ingresar al area reservada')
        return redirect(url_for('main.index'))

@bp.app_errorhandler(404)
def page_not_found(error):
    print(error)
    return render_template('page_not_found.html'), 404