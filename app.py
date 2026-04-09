"""Simple Flask application for CI/CD demo."""
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def hello():
    """Return hello message."""
    return jsonify({'message': 'Hello, CI/CD World!'})


@app.route('/health')
def health():
    """Health check endpoint."""
    return jsonify({'status': 'healthy'})


@app.route('/add')
def add():
    """Add two numbers using query parameters."""
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    return jsonify({'result': a + b})


@app.route('/subtract')
def subtract():
    """Subtract two numbers using query parameters."""
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    return jsonify({'result': a - b})


@app.route('/multiply')
def multiply():
    """Multiply two numbers using query parameters."""
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    return jsonify({'result': a * b})


@app.route('/divide')
def divide():
    """Divide two numbers using query parameters."""
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    if b == 0:
        return jsonify({'error': 'Cannot divide by zero'}), 400
    return jsonify({'result': a / b})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
