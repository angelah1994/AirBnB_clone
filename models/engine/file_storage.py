#!/usr/bin/env python3
"""
'file_storage' module
"""
import json
import os.path


class FileStorage:
    """
    serializes instances to a JSON file and deserializes JSON\
    files to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        if obj is not None:
            obj_id = type(obj).__name__ + "." + obj.id
            self.__objects[obj_id] = obj

    def save(self):
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()

        with open(self.__file_path, "w") as f:
            json.dump(my_dict, f)

    def reload(self):
        classes = {"BaseModel" : "models.base_model.BaseModel"}
        try:
            with open(self.__file_path, "r") as f:
                json_load = json.load(f)
                for key in json_load:
                    self.__objects[key] = classes[json_load[key]["__class__"]](**json_load[key])

        except Exception:
            return
                 
