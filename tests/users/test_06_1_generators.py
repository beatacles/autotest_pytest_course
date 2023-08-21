"""Генерируем тестовые данные для тестов"""
import pytest

from src.generators.player_localization import Player_localization


@pytest.mark.parametrize("status", ["ACTIVE", "BANNED", "DELETED", "INACTIVE"])
def test_user_generator_status(status, get_generated_player):
    print(get_generated_player.set_status(status).build())


@pytest.mark.parametrize("balance", ["-1", "0", "100", "adsa"])
def test_user_generator_balance(balance, get_generated_player):
    print(get_generated_player.set_balance(balance).build())


def test_user_generator_update_data(get_generated_player):
    object_to_send = get_generated_player.update_inner_value(
        ['localize', 'en', 'countries'], Player_localization('fr_FR').build()).build()
    print(object_to_send)


@pytest.mark.parametrize("localizations", ['fr', 'de', 'it', 'cn'])
def test_user_generator_update_data(get_generated_player, localizations):
    object_to_send = get_generated_player.update_inner_value(
        ['localize', localizations], Player_localization('fr_FR').build()).build()
    print(object_to_send)
