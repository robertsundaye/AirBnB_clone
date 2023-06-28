#!/usr/bin/python3

import datetime
class BaseModel:
    def __init__(self, id = uuid.d4(), created_at = datetime.datetime.today(), updated_at = datetime.datetime.today()):
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        print("BaseModel")
        print(self.id)
        print(self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.today()

    def to_dict(self):
        return self.__dict__()
