#!usr/bin/env python3
"""base model file"""
import uuid
import datetime
import json
from models import storage


class BaseModel:
    """
    base model from which all other classes will inherit
    """
    number_of_instances = 0

    def __init__(self, *args, **kwargs):
        if kwargs:
            self.__dict__ = json.loads(json.dumps(kwargs))
            self.__dict__['created_at'] = datetime.datetime.strptime(self.__dict__['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
            self.__dict__['updated_at'] = datetime.datetime.strptime(self.__dict__['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
            del self.__dict__['__class__']
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)
            storage.save()

    def __str__(self):
        return "[{}] ({}) {}\
".format(str(type(self).__name__), str(self.id), self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        my_dict = self.__dict__.copy()
        my_dict['created_at'] = self.__dict__['created_at'].strftime("%Y-%m-%dT%H:%M:%S.%f")
        my_dict['updated_at'] = self.__dict__['updated_at'].strftime("%Y-%m-%dT%H:%M:%S.%f")
        my_dict['__class__'] = type(self).__name__
        return my_dict
