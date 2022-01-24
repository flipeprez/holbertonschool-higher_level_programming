#!/usr/bin/python3
class Rectangle:
    '''define rectangle class'''
    number_of_instances = 0
    print_symbol = "#"
    
    def __init__(self, width=0, height=0):
        '''def func'''
        self.height = height
        self.width = width
        number_of_instance = 0
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        '''define property'''
        return self.__width

    @width.setter
    def width(self, value):
        '''define width setter'''
        if type(value) is not int:
            raise TypeError("width must be a integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''define prperty'''
        return self.__height

    @height.setter
    def height(self, value):
        '''define height setter'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        '''define area self'''
        return self.width * self.height

    def perimeter(self):
        '''define perimeter'''
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        '''define string to print'''
        rec = ""
        if self.width == 0 or self.height == 0:
            return rec
        for g in range(self.height):
            for t in range(self.width):
                rec += str(self.print_symbol)
            if g is not self.height - 1:
                rec += "\n"
        return rec

    def __repr__(self):
        '''define repr'''
        return (type(self).__name__ + "(" + str(self.__width) + "," +
                str(self.__height) + ")")
    def __del__(self):
        '''def del'''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
    
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        ''' define static method'''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        elif rect_1.area() >= rect_2.area():
            return rect_1
