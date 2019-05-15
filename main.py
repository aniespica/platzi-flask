from flask import Flask, request, make_response, redirect, render_template, session
import unittest

app = Flask(__name__)

app.config['SECRET_KEY'] = 'SUPER SECRETO'


todos = ['Buy coffee', 'Buy game', 'Buy milk ']

@app.cli.command()
def test():
  tests = unittest.TestLoader().discover('tests')
  unittest.TextTestRunner().run(tests)

@app.errorhandler(404)
def not_found(error):
  return render_template('404.html', error=error)

@app.route('/')
def index():
  user_ip = request.remote_addr

  response = make_response(redirect('/hello'))
  session['user_ip'] = user_ip
  
  return response


@app.route('/hello')
def hello():
  user_ip = session.get('user_ip')
  context = {
    'user_ip':user_ip,
    'todos':todos
  }

  return render_template('hello.html', **context)
