#!/usr/bin/python3

""" sql alchemy """
from sqlalchemy import Sequence, Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """ City object """
    __tablename__ = 'cities'
    id = Column(
        Integer,
        Sequence('my_sequence'),
        primary_key=True,
        nullable=False,
        )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
