import requests
import pytest

def test_get_products():
    """Test your function"""
    url = "https://fakestoreapi.com/products"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        
        assert response.status_code == 200
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
        
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Your request has failed: {e}")
        