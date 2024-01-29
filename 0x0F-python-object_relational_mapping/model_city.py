#!/usr/bin/python3
"""City model module"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """City Class that inherits from Base"""
    __tablename__ = "cities"

    id = Column("id", Integer, nullable=False, autoincrement=True,
                primary_key=True)
    name = Column("name", String(128), nullable=False)
    state_id = Column("state_id", Integer, ForeignKey('states.id'),
                      nullable=False)

