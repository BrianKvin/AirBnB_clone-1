#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import column. string
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes
    __table__name(str): The name of the MySQL table to store users.
    email: (sqlalchemy string):The user's email address.
    password (sqlalchemy string): The user's password
    first_name (sqlalchemy string): The user's first name
    last_name (sqlalchemy string): The user's last name
    places (sqlalchemy relationship): The user-place relationship
    reviews (sqlalchemy relationship): The user-Review relationship
    """   
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
