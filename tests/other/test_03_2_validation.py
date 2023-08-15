"""Запрос к ресурсу. Проверка status code. Валидация json через базовый класс"""
import requests

from config import SERVICE_URL
from src.base_classes.response import Response

def test_getting_posts():
    r = requests.get(url = SERVICE_URL)
    response = Response(r)
