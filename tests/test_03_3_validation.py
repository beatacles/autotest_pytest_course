"""Запрос к ресурсу. Проверка status code. Валидация json через pydantic"""
import requests

from config import SERVICE_URL
from src.base_classes.response import Response_pydantic
from src.pydantic_schemas.post import Post

def test_getting_posts():
    r = requests.get(url = SERVICE_URL)
    response = Response_pydantic(r)
    response.assert_status_code(200).validate(Post)
