#!/usr/bin/python3
"""Module for the filestorage class"""

import datetime
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City


class FileStorage:
    """Class for storing, serializing and deserializing data"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects.
        and acess to  all the stored objects.

        """
        return FileStorage.__objects

    def new(self, obj):
        """
         sets in __objects the obj with key <obj class name>.id
        """

        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)
        """
        all_obj = FileStorage.__objects
        d = {}

        for obj in all_obj.keys():
            d[obj] = all_obj[obj].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(d, f)

    def reload(self):
        """
        Method that deserializes the JSON file to __objects
        """
        if not os.path.isfile(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            for key, value in obj_dict.items():
                FileStorage.__objects = obj_dict
        except Exception:
            pass
