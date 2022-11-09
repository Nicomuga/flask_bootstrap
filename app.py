from flask import Flask, request, render_template 


app = Flask(__name__)


@app.route('/')

def hello_world():
  return 'helrutas = app.url_maplo worldie'


@app.route('/usuario/<name>')
def user(name):
  return render_template('user.html', name = name)



@app.route('/navegador')
def browser():
  user_agent = request.headers.get('User-Agent')
  return f'Tu navegafor es: {user_agent}'

@app.route('/rutas')
def routes():
  
  print(app.url_map)
  return 'revisa tu consola para ver las rutas'



if __name__ == '__main__':
  app.run(ssl_context='adhoc')


