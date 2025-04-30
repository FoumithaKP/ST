import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_addition(client):
    response = client.post('/calculate', data={'num1': '10', 'num2': '5', 'operation': 'add'})
    assert b'15.0' in response.data

def test_subtraction(client):
    response = client.post('/calculate', data={'num1': '10', 'num2': '5', 'operation': 'subtract'})
    assert b'5.0' in response.data

def test_multiplication(client):
    response = client.post('/calculate', data={'num1': '10', 'num2': '5', 'operation': 'multiply'})
    assert b'50.0' in response.data

def test_division(client):
    response = client.post('/calculate', data={'num1': '10', 'num2': '5', 'operation': 'divide'})
    assert b'2.0' in response.data

def test_division_by_zero(client):
    response = client.post('/calculate', data={'num1': '10', 'num2': '0', 'operation': 'divide'})
    assert b'Result: Division by zero is not allowed' in response.data
