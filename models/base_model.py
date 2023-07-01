#!/usr/bin/python3
"""creating a base model"""

import datetime
import uuid

class BaseModel:
    """Parent class"""
    def __init__(self, *args, **kwargs):
        """
        Arg:
        id: str -- contain unique string using uuid4()
        created_at: str -- time when an instance is created
        updated_at: str -- set to present date when the save function is called
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                     setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.ddatetime.today()
            self.updated_at = self.created_at

    def __str__(self):
        """print every class and instances in dict form"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """update self.update_at to current time"""
        self.updated_at = datetime.datetime.today()

    def to_dict(self):
        """return a dict object"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict