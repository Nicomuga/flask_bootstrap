from app.auth import bp
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_login import login_user,logout_user, login_required
from app.models.user import User
from app.extensions import db

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
            user = User(email = email , username = username,password = password)
            db.session.add(user)
            db.session.commit()
            flash('usuario creado correctamente')
            return redirect(url_for('auth.index'))
    return render_template('auth/register.html')

@bp.route('/login', methods = ('GET','POST'))
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        remember = request.form.get('remember_me')
        if not email:
                flash('El correo es requerido')
        elif not password:
                flash('La password es requerida')

        else:
            user = User.query.filter_by(email=email).first()
            if user and user.verify_password(password):
                login_user(user, remember)
                next = request.args.get('next')
                if next is None or not next.startswith('/'):
                    next = url_for('main.index')
                flash(f'Bienvenido {user.username}')    
                return redirect(next)
            flash('usuario o password incorrecto')
    return render_template('auth/login.html')

@bp.route('logout')
@login_required
def logout():
    logout_user()
    flash('Sesión cerrada')
    return redirect('/auth/login')

@bp.app_errorhandler(404)
def page_not_found(error):
        return render_template('page_not_found.html'), 404