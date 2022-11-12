from flask import Flask, request, render_template 


app = Flask(__name__)


@app.route('/')
def hello_world():
  return render_template('index.html')


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



