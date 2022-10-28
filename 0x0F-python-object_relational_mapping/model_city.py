#!/usr/bin/python3
"""
    Write a python file that contains the class
    definition of a State and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
        Cities class
    """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, primary_key=True,
                unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
