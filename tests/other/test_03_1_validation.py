"""Запрос к ресурсу. Проверка status code. Проверка длинны json. Валидация json через схему"""
import requests
from jsonschema import validate

from config import SERVICE_URL
from src.enums.global_enums import GlobalErrorMessages
from src.schemas.post import POST_SCHEMA

def test_getting_posts():
    response = requests.get(url = SERVICE_URL)
    recieved_posts = response.json()

    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    assert len(recieved_posts) == 3, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value
    for post in recieved_posts:
        validate(post, POST_SCHEMA)
