#!/usr/bin/env python
from flask import Flask, request
import hashlib

app = Flask(__name__)

def generate_unique_id():
    ip_address = request.remote_addr  # Get user's IP address
    unique_id = hashlib.md5(ip_address.encode()).hexdigest()  # Generate unique ID using IP address
    return unique_id

@app.route('/')
@app.route('/hello')
@app.route('/hello/')
def hello_world():
    host_id = generate_unique_id()  # Generate a unique host ID based on user's IP address
    return 'Hello World! Host ID: {}\n'.format(host_id)

@app.route('/hello/<username>')
def hello_user(username):
    host_id = generate_unique_id()  # Generate a unique host ID based on user's IP address
    return 'Why Hello %s! Host ID: %s\n' % (username, host_id)

if __name__ == '__main__':
    app.run(host='0.0.0.0' port=5000)

