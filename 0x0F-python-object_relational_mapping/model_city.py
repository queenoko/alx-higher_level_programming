#!/usr/bin/python3
"""
The script that defines a City class
to work with MySQLAlchemy ORM....
"""
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """The City class
    Attributes:
        __tablename__ (str): The table name of the class
        id (int): The id of the class city
        name (str): The name of the class
        state_id (int): The state the city will belong...
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
