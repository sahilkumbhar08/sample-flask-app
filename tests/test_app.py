from app import app
import pytest

def test_hello_endpoint():
    with app.test_client() as client:
        response = client.get('/hello')
        assert response.status_code == 200
        assert response.data.decode('utf-8') == 'Hello, World!'

def test_broken_endpoint():
    with app.test_client() as client:
        response = client.get('/hello')
        assert response.data.decode('utf-8') == 'Hello, World One!'  # Intentionally wrong; AI can fix by changing to 'Hello, World!'
