"""Запрос к ресурсу через фикстуру. Проверка status code. Валидация json через pydantic."""


from src.base_classes.response import Response_pydantic
from src.pydantic_schemas.user import User


def test_getting_users_list(get_users):
    Response_pydantic(get_users).assert_status_code(200).validate(User)
