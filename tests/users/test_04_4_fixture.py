"Setup - Teardown"


def test_get_number_after_calulcate(make_number):
    assert 1==1
    print(make_number)

# tests/users/test_04_4_fixture.py::test_get_number_after_calulcate im getting number - фикстура создала число и print
# None - если в yield ничего не передовали в тест. И число, если передавали
# PASSEDNumber at home 901 - вернулись в фистуру,  print сгенерированного числа
