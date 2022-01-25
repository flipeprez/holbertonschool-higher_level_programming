#!/usr/bin/python3
"""module doc"""


class Rectangle:
    """class doc"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """init doc"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        elif not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.height = height
            self.width = width
            Rectangle.number_of_instances += 1

    @property
    def width(self):
        """width getter doc"""
        return self.__width

    @property
    def height(self):
        """height getter doc"""
        return self.__height

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    def area(self):
        """area doc"""
        return self.__height * self.__width

    def perimeter(self):
        """perimeter doc"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """str doc"""
        if self.__width == 0 or self.__height == 0:
            return ""
        string = ""
        for i in range(self.__height):
            for j in range(self.__width):
                string += str(self.print_symbol)
            if i is not self.__height - 1:
                string += "\n"
        return string

    def __repr__(self):
        """repr doc"""
        return (type(self).__name__ + "(" + str(self.__width) + ", " +
                str(self.__height) + ")")

    def __del__(self):
        """del doc"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """bigger_or_equal doc"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if Rectangle.area(rect_2) > Rectangle.area(rect_1):
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """square doc"""
        return cls(size, size)
