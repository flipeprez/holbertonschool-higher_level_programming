#!/usr/bin/python3
'''def class'''
import json


class Base:
    '''def class attribute'''
    __nb_objects = 0

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
        '''def create method'''
        if cls.__name__ == "Rectangle":
            r1 = cls(6, 7)
        elif cls.__name__ == "Square":
            r1 = cls(8)
        r1.update(**dictionary)
        return r1

    @classmethod
    def load_from_file(cls):
        '''def fun load from file'''
        e_list = []
        nfile = f"{cls.__name__}.json"
        if path.isfile(f"{cls.__name__}.json"):
            with open(nfile, "r") as f:
                for line in f:
                    try:
                        instance = cls.from_json_string(line)
                        for item in instance:
                            e_list.append(cls.create(**item))
                    except Exception as e:
                        print(f"Error")
        return e_list

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return ([])
        else:
            return json.loads(json_string)
