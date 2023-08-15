"""Запрос к ресурсу. Проверка status code. Проверка длинны json"""
import requests
from config import SERVICE_URL
from src.enums.global_enums import GlobalErrorMessages

def test_getting_posts():
    response = requests.get(url = SERVICE_URL)
    recieved_posts = response.json()

    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    assert len(recieved_posts) == 3, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value
