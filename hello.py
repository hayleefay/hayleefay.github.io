# export FLASK_DEBUG=1
# flask run

from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello_world():
    return 'Hello, world!'

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username
