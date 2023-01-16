#!/usr/bin/python3
import json
"""Class declaration """


class Base:
    """A class that defines objects """
    __nb_objects = 0

    def __init__(self, id=None):
        """instasiation of objects with attribute"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """converts a dict to json string"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"

        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save json rep to a file"""
        file_n = cls.__name__ + ".json"
        with open(file_n, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                f.write(Base.to_json_string(list_dicts))
