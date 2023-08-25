from sqlalchemy import Boolean, Column, Integer, String
from db import Model


class Person(Model):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    second_name = Column(String)
