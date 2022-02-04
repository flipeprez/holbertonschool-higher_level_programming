#!/usr/bin/python3
'''def class'''
import json


class Base:
    '''def class attribute'''
    __nb_objects= 0

    def __init__(self, id=None):
        '''def class init'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def save_to_file(cls, list_objs):
        '''comment'''
        new_list = []
        name = str(cls.__name__) + ".json"
        with open(name, "w") as f:
            if list_objs is None:
                f.write(cls.to_json_string(new_list))
            else:
                for obj in list_objs:
                    new_list.append(cls.to_dictionary(obj))
                f.write(cls.to_json_string(new_list))

    @classmethod
    def create(cls, **dictionary):
        from models.rectangle import Rectangle
        if cls.__name__ == "rectangle":
            r1 = Rectangle(10, 7, 2, 8)
            return r1
    
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return "[]"
        else:
            return json.dumps(json_string)
