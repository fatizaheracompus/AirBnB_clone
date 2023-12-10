#!/usr/bin/python3
"""Module that creates the user class"""

from models.base_model import BaseModel


class User(BaseModel):
    """Class represent the user objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
