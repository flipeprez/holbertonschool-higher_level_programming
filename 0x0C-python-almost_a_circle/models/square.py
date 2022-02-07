#!/usr/bin/python3
'''def square'''


from models.rectangle import Rectangle


class Square(Rectangle):
    '''def square'''
    def __init__(self, size, x=0, y=0, id=None):
        '''def class constructor'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''def str overloading'''
        return f"[Square] ({self.id}) {self.x}/{self.y}\
 - {self.width}"

    def update(self, *args, **kwargs):
        '''def update method'''
        attr = {0: "id", 1: "size", 2: "x", 3: "y"}
        if args:
            if len(args) < 5:
                for i in range(len(args)):
                    setattr(self, attr[i], args[i])
        else:
            for k in kwargs:
                setattr(self, k, kwargs[k])

    def to_dictionary(self):
        '''def to dictionary'''
        dictionary = {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
        }
        return dictionary

    @property
    def size(self):
        '''def size prop'''
        return self.width

    @size.setter
    def size(self, size):
        '''def size setter'''
        self.width = size
        self.height = size
