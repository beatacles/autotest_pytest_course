"""Генерируем тестовые данные для тестов"""
import pytest

@pytest.mark.parametrize("status", ["ACTIVE", "BANNED", "DELETED", "INACTIVE"])
def test_user_generator(status, get_generated_player):
    print(get_generated_player.set_status(status).build())

@pytest.mark.parametrize("balance", ["-1", "0", "100", "adsa"])
def test_user_generator(balance, get_generated_player):
    print(get_generated_player.set_balance(balance).build())