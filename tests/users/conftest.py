import pytest

from random import randrange
@pytest.fixture
def get_random_number():
    return randrange(1,1000,5)