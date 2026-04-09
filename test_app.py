"""Unit tests for the Flask application."""
import pytest
from app import app


@pytest.fixture
def client():
    """Create a test client."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_hello(client):
    """Test the hello endpoint."""
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'Hello, CI/CD World!'


def test_health(client):
    """Test the health endpoint."""
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'


def test_add(client):
    """Test the add endpoint."""
    response = client.get('/add/3/5')
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == 8


def test_add_negative(client):
    """Test adding negative numbers."""
    response = client.get('/add/-3/-5')
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == -8


def test_subtract(client):
    """Test the subtract endpoint."""
    response = client.get('/subtract/10/3')
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == 7


def test_subtract_negative(client):
    """Test subtracting negative numbers."""
    response = client.get('/subtract/5/-3')
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == 8


def test_multiply(client):
    """Test the multiply endpoint."""
    response = client.get('/multiply/4/5')
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == 20


def test_multiply_negative(client):
    """Test multiplying negative numbers."""
    response = client.get('/multiply/-3/-4')
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == 12


def test_multiply_by_zero(client):
    """Test multiplying by zero."""
    response = client.get('/multiply/5/0')
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == 0
