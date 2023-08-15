import pytest
import requests
from config import API_URL, SERVICE_URL


@pytest.fixture
def get_users():
    response = requests.get(API_URL)
    return response

def _calculate(a,b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        return None

@pytest.fixture
def calculate():
    return _calculate

