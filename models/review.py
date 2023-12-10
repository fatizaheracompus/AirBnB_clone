#!/usr/bin/python3
"""Module that creates the review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class represent the review object"""

    place_id = ""
    user_id = ""
    text = ""
