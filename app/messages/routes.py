from app.messages import bp
from flask import Flask, redirect, render_template,request, url_for, flash
from app.models.message import Message
from app.models.user import User
from app.extensions import db, migrate
from flask_login import login_required, current_user


@bp.route('/')
@login_required
def index():
  '''m_user_id = User.query.filter_by(username = str(current_user)).first()
  print(m_user_id)'''
 
  print(current_user)
  messages = Message.query.filter_by(user = current_user).all()
  return render_template('messages/index.html', messages = messages)



@bp.route('/create', methods = ('GET','POST'))
@login_required
def create():
  if request.method == 'POST':
    title = request.form['title']
    content = request.form['content']
    picture = request.form['picture']
    if not title:
      flash('el titulo es requerido')
    elif not content:
      flash('el contenido es requerido')
    else:
      message = Message(title = title , content = content, picture = picture, user = current_user)
      db.session.add(message)
      db.session.commit()
      return redirect(url_for('messages.index'))
  return render_template('messages/create.html')

@bp.route('/delete', methods = ['POST'])
@login_required
def delete():
    id = request.form['id']
    message = Message.query.filter_by(id=id).first()
    db.session.delete(message)
    db.session.commit()
    flash('Mensaje Eliminado')
    return redirect(url_for('messages.index'))


@bp.route('/<id>/update', methods = ('GET', 'POST'))
@login_required
def update(id):
  message = Message.query.filter_by(id=id).first()
  if request.method == 'POST':
    if message:
      message.title = request.form['title']
      message.picture = request.form['picture']
      message.content = request.form['content']
      if len(message.title) > 0 or len(message.content) > 0:
        db.session.commit()
        return redirect(url_for('messages.index'))
      else: 
        flash('El titulo y/o contenido son requeridos')
  return render_template('messages/update.html', message = message)

