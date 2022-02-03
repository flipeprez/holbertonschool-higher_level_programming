#!/usr/bin/python3
'''def rectngle'''


from models.base import Base


class Rectangle(Base):
    '''def rectangle'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''init method'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        '''def area instance'''
        return self.width * self.height

    def display(self):
        '''print area'''
        stry = "\n" * self.y
        print(stry, end= "")
        for i in range(self.height):
            strx= " " * self.x
            print (strx, end="")
            strwidth = "#" * self.width
            print(strwidth)

    def __str__(self):
        '''def str'''
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y}\
- {self.__width}/{self.__height}"

    def update(self, *args):
        '''def update method'''
        attr={0:"id", 1:"width", 2:"height", 3:"x", 4:"y"}
        if len(args) < 5:
            for i in range(len(args)):
                setattr(self, attr[i], args[i])

    @property
    def width(self):
        '''def width property'''
        return self.__width

    @width.setter
    def width(self, width):
        '''def width setter'''
        if width is not type(int):
            TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        '''def height property'''
        return self.__height

    @height.setter
    def height(self, height):
        '''def height setter'''
        if height is not type(int):
            TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        '''def x property'''
        return self.__x

    @x.setter
    def x(self, x):
        if x is not type(int):
            TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        '''def y property'''
        return self.__y

    @y.setter
    def y(self, y):
        '''def y setter'''
        if y is not type(int):
            TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y
