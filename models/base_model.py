#!/usr/bin/python3
"""BaseModel that defines all common attributes/methods"""

import uuid
from datetime import datetime
from  models import storage


class BaseModel:
    """Class defines all common attributes for other class"""

    def __init__(self, *args, **kwargs):
        """Method that initialize instance attribuer"""

        tm_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                            kwargs["created_at"], tm_format)
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                            kwargs["updated_at"], tm_format)
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            storage.new(self)

    def __str__(self):
        """Should print official string representation"""
        class_name = self.__class__.name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at with c time
        """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """ returns a dictionary contanain key
        """
        int_dict = self.__dict__.copy()
        int_dict["__class__"] = type(self).__name__
        int_dict["created_at"] = self.created_at.isoformat()
        int_dict["updated_at"] = self.updated_at.isoformat()
        return int_dict
