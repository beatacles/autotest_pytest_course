import pytest
import requests
import tables
from config import API_URL, SERVICE_URL
from src.generators.player import Player
from src.generators.item import ItemTypeBuilder
from db import Session


@pytest.fixture
def get_users():
    response = requests.get(API_URL)
    return response


def _calculate(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        return None


@pytest.fixture
def calculate():
    return _calculate


@pytest.fixture
def get_generated_player():
    return Player()


@pytest.fixture
def get_db_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()


def delete_test_data(Session, table, filter_data):
    Session.query(table).filter(filter_data).delete()
    Session.commit()


@pytest.fixture
def get_delete_method():
    return delete_test_data


def create_method(Session, item):
    Session.add(item)
    Session.commit()


@pytest.fixture
def get_create_method():
    return create_method


@pytest.fixture
def get_item_type_generator():
    return ItemTypeBuilder()

@pytest.fixture
def generate_item_type(get_db_session, get_item_type_generator, get_create_method, get_delete_method):
    item = tables.ItemType(**get_item_type_generator.build())
    get_create_method(get_db_session, item)
    yield item
    get_delete_method(get_db_session,tables.ItemType,
                      (tables.ItemType.item_id == item.item_id))



