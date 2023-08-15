"""Параметризация при помощи pytest. Кастомные маркеры(pytest.ini)"""
"""Запуск: -k название маркера. Если использовать маски: -л 'not название маркера'"""
"""-vv durations= время в секундах.  Позволяет увидеть тесты длящиеся более указанного времени"""


import pytest


@pytest.mark.skip("don't need because parametrizer is work")
def test_calculation_positive_positive(calculate):
    print(calculate(1, 2))


@pytest.mark.skip("don't need because parametrizer is work")
def test_calculation_positive_negative(calculate):
    print(calculate(1, -2))


@pytest.mark.skip("don't need because parametrizer is work")
def test_calculation_negative_negative(calculate):
    print(calculate(-1, -2))


@pytest.mark.skip("don't need because parametrizer is work")
def test_calculation_char_number(calculate):
    print(calculate("a", -2))


@pytest.mark.skip("don't need because parametrizer is work")
def test_calculation_char_char(calculate):
    print(calculate("a", "b"))


@pytest.mark.development
@pytest.mark.production
@pytest.mark.parametrize('first_value, second_value, result', [
    (1, 2, 3),
    (-1, 2, 1),
    (0, 5, 5),
    ('b', 2, None),
    ('b', 'b', None)
])
def test_calculator(first_value, second_value, result, calculate):
    assert calculate(first_value, second_value) == result
