"""Simple Flask application for CI/CD demo."""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    """Return hello message."""
    return jsonify({'message': 'Hello, CI/CD World!'})


@app.route('/health')
def health():
    """Health check endpoint."""
    return jsonify({'status': 'healthy'})


@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    """Add two numbers."""
    return jsonify({'result': a + b})


@app.route('/subtract/<int:a>/<int:b>')
def subtract(a, b):
    """Subtract two numbers."""
    return jsonify({'result': a - b})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
