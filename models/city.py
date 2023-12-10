#!/usr/bin/python3
"""The module create the city class"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class represent the city object"""

    state_id = ""
    name = ""
