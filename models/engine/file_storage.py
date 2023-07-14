#!/usr/bin/python3
"""
FileStorage module:
"""
import json
from models.base_model import BaseModel

class FileStorage:
    """
     a class FileStorage that serializes instances to a JSON file and
     deserializes JSON file to instances:
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        This returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        This method sets in __objects the obj with key <obj class name>.id
        """
        if obj is not None:
            FileStorage.__objects[obj.__class__.__name__ + "." + str(obj.id)] = obj

    def save(self):
        """
        method serializes __objects to the JSON file
        """
        Ocopy = FileStorage.__objects
        obj_dict = {obj: Ocopy[obj].to_dict() for obj in Ocopy.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)
        # with open(FileStorage.__file_path, "w", encoding='utf-8') as file:
        #     new_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        #     json.dump(new_dict, file)
        
    def reload(self):
        """
        This method deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
