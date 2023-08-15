"""Разграничение conftest. Проверка фикстур. Добавление вспомогательных функций для фикстур"""


def test_get_number_after_calulcate(calculate):
    assert 1==1
    print(calculate)
    print(calculate(1, 1))
