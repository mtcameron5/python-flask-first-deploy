## BUILDPACK NECESSARY
## heroku buildpacks:set heroku/python
## heroku buildpacks:remove heroku/python

from flask import Flask, gunicorn, escape, url_for, render_template, request

app = Flask(__name__)

@app.route('/') 
def index():
  return 'Index page'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
  return render_template('hello.html', name=name)

@app.route('/login', methods=['POST', 'GET'])
def login():
  error = None
  if request.method == 'POST':
    if valid_login(request.form['username'], request.form['password']):
      return log_the_user_in(request.form['username'])
    else:
      error = 'Invalid username/password'
  return render_template('login.html', error=error)

@app.route('/user/<username>') 
def profile(username):
  return '{}\'s profile'.format(escape(username))

with app.test_request_context():
  print(url_for('index'))
  print(url_for('login'))
  print(url_for('login', next='/'))
  print(url_for('profile', username='mtcameron3'))

