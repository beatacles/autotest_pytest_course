from sqlalchemy import Boolean, Column, Integer, String
from db import Model


class Person(Model):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    second_name = Column(String)


class ItemType(Model):
    __tablename__ = 'item_type'
    item_id = Column(Integer, primary_key = True)
    item_type = Column(String)
