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
    response = client.get('/add?a=3&b=5')
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == 8


def test_add_negative(client):
    """Test adding negative numbers."""
    response = client.get('/add?a=-3&b=-5')
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == -8


def test_subtract(client):
    """Test the subtract endpoint."""
    response = client.get('/subtract?a=10&b=3')
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == 7


def test_subtract_negative(client):
    """Test subtracting negative numbers."""
    response = client.get('/subtract?a=5&b=-3')
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == 8


def test_multiply(client):
    """Test the multiply endpoint."""
    response = client.get('/multiply?a=4&b=5')
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == 20


def test_multiply_negative(client):
    """Test multiplying negative numbers."""
    response = client.get('/multiply?a=-3&b=-4')
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == 12


def test_multiply_by_zero(client):
    """Test multiplying by zero."""
    response = client.get('/multiply?a=5&b=0')
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == 0


def test_divide(client):
    """Test the divide endpoint."""
    response = client.get('/divide?a=20&b=4')
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == 5.0


def test_divide_negative(client):
    """Test dividing negative numbers."""
    response = client.get('/divide?a=-20&b=4')
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == -5.0


def test_divide_by_zero(client):
    """Test dividing by zero returns error."""
    response = client.get('/divide?a=20&b=0')
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data
    assert 'Cannot divide by zero' in data['error']
