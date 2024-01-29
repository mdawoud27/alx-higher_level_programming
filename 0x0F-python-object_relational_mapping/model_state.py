#!/usr/bin/python3
"""the class definition of a State module"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class that is an instance of Base"""
    __tablename__ = "states"

    id = Column("id", Integer, primary_key=True,
                autoincrement=True, nullable=False)
    name = Column("name", String(128), nullable=False)

    def __init__(self, name):
        """Initialization method"""
        self.name = name
