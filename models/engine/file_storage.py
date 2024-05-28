#!/usr/bin/python3
"""
Module for serializing and deserializing data to and from a file storage
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.amenty import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        serialized_obj = {}
        for key, value in FileStorage.__objects.items():
            serialized_obj[key] = value.to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as json_f:
            json.dump(serialized_obj, json_f)

    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, encoding="utf-8") as json_f:
                try:
                    obj_dict = json.load(json_f)
                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split('.')
                        Cls = eval(class_name)
                        obj = Cls(**value)
                        FileStorage.__objects[key] = obj
                except FileNotFoundError:
                    pass
