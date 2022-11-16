from flask import Flask, request, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



app = Flask(__name__)
app.config['SECRET_KEY'] = 'cualquier cosa'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://muga:5543@localhost:5432/flask_bootstrap'

db = SQLAlchemy(app)
migrate = Migrate(app,db)

class Message(db.Model):
  __tablename__ = 'messages'
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(128), nullable=False)
  content = db.Column(db.Text, nullable=False)

  def __repr__(self):
    return f'<message {self.title}>'

@app.route('/')
def index():
  messages = Message.query.all()
  return render_template('index.html', messages = messages)

@app.route('/create', methods = ('GET','POST'))
def create():
  if request.method == 'POST':
    title = request.form['title']
    content = request.form['content']
    if not title:
      flash('el titulo es requerido')
    elif not content:
      flash('el contenido es requerido')
    else:
      message = Message(title = title , content = content)
      db.session.add(message)
      db.session.commit()
      return redirect(url_for('index'))
  return render_template('create.html')

@app.route('/usuario/<name>')
def user(name):
  return render_template('user.html', name = name)

@app.route('/usuario')
def stranger():
  return render_template('user.html')


@app.route('/navegador')
def browser():
  user_agent = request.headers.get('User-Agent')
  return f'Tu navegafor es: {user_agent}'

@app.route('/rutas')
def routes():
  
  print(app.url_map)
  return 'revisa tu consola para ver las rutas'

@app.errorhandler(404)
def page_not_found(error):
  return render_template('page_not_found.html'), 400



