from flask import Flask, render_template
import os
import platform
import socket

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/health')
def health():
    return {
        'status': 'healthy', 
        'port': 8080,
        'hostname': socket.gethostname(),
        'platform': platform.platform()
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)