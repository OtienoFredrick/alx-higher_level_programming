#!/usr/bin/python3
"""
This script defines a State class and
a Base class to work with MySQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declaratie import declarative_base

Base = declarative_base()


class State(Base):
    """State class

    Attributes:
    __tablename__(str): The table name of the class
    id (int): The state id of the class
    name (str): The state name of the class
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
