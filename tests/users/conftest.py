import pytest

from random import randrange


@pytest.fixture
def get_random_number():
    return randrange(1, 1000, 5)


"Setup - Teardown"
"Используется для подключение к БД. Создали объект в БД, сделали тест и удалили"


@pytest.fixture
def make_number():
    # print("im getting number")
    number = randrange(1, 1000, 5)
    yield number  # по сути return с разрывом
    # print(f"Number at home {number}")
