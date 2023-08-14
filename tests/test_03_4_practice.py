"""Запрос к ресурсу. Проверка status code. Валидация json через pydantic"""
import requests
from config import API_URL, SERVICE_URL
from src.base_classes.response import Response_pydantic
from src.pydantic_schemas.user import User


def test_getting_users_list():
    response = requests.get(API_URL)
    test_object = Response_pydantic(response)
    test_object.assert_status_code(300).validate(User)
