from app.messages import bp
from flask import Flask, redirect, render_template,request, url_for, flash
from app.models.message import Message
from app.models.sizelink import Sizelink
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
    type_of = request.form['type_of']
   

    if not title:
      flash('el titulo es requerido')
    elif not content:
      flash('el contenido es requerido')
    elif not type_of:
      flash('el tipo es requerido') 
    
    else:
      message = Message(title = title , content = content, picture = picture, user = current_user, type_of = type_of)
      db.session.add(message)
      db.session.commit()
      return redirect(url_for('messages.index'))
  return render_template('messages/create.html')


@bp.route('/create_size', methods = ('GET','POST'))
@login_required
def create_size():
  if request.method == 'POST':
   
    link = request.form['link']
    price = request.form['price']
    size = request.form['size'] 

    if not link:
      flash('el link es requerido')
    elif not price:
      flash('el price es requerido')
    elif not size:
      flash('el size es requerido') 
    
    else:
      sizelink = Sizelink(link = link , price = price, size = size)
      db.session.add(sizelink)
      db.session.commit()
      flash('tamaño agregado')
      return redirect('messages/create_size')
  return render_template('messages/create_size.html')

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

