from app.auth import bp
from flask import Flask, render_template, request, flash, redirect, url_for
from app.models.user import User
from app.extensions import db, migrate

@bp.route('/')
def index():
    users = User.query.all()
    return render_template('auth/index.html', users=users)

@bp.route('/register', methods = ('GET','POST'))
def register():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        password_confirm = request.form['password_confirm']
        if not email:
            flash('El correo es requerido')
        elif not username:
            flash('El nombre de usuario es requerido')
        elif not password:
            flash('La password es requerida')
        elif not password == password_confirm:
            flash('Las contrase;as no coinciden')
        else:
            user = User(email = email , username = username,password_hash= password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.index'))
    return render_template('auth/register.html')