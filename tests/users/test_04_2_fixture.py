"""Разграничение conftest. Проверка фикстур"""


def test_getting_number(get_random_number):
    assert 1==1
    print(get_random_number)
