#!/usr/bin/env python
from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
@app.route('/hello')
@app.route('/hello/')
def hello_world():
    return 'Hello World!\n'

@app.route('/hello/<username>')
def hello_user(username):
    return 'Why Hello %s!\n' % username
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80) 

    # Run the Flask app with the dynamically generated IP address
    app.run(host=host_ip, port=5000)
