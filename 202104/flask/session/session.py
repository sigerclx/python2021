#!/usr/bin/python3
from flask import Flask, session, render_template
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

def query():
    user = session.get('user')
    user1 = session.get('user1')

    return render_template('query.html', user = user,user1 = user1)

@app.route('/set')
def set():
    session['user'] = 'tom'
    session['user1'] = 'jacky'
    return query()

@app.route('/get')
def get():
    return query()

@app.route('/del')
def delete():
    session.pop('user')
    return query()

@app.route('/clear')
def clear():
    session.clear()
    return query()

if __name__ == '__main__':
    app.run(debug=True)