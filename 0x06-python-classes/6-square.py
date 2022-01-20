#!/usr/bin/python3
'''lala'''


class Square:
    '''lala'''
    def __init__(self, size=0, position=(0, 0)):
        '''lala'''
        self.__size = size
        self.__position = position

    @property
    def size(self):
        '''lalal'''
        return self.__size

    @size.setter
    def size(self, value):
        '''lalal'''
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        '''lalala'''
        return self.__size * self.__size

    def my_print(self):
        '''lalal'''
        if self.__size == 0:
            print()
        for i in range(self.__position[1]):
            print()
        for o in range(self.__size):
            for g in range(self.__position[0]):
                print(" ", end="")
            for t in range(self.__size):
                print("#", end="")
            print()

    @property
    def position(self):
        '''lalal'''
        return self.__position

    @position.setter
    def position(self, value):
        '''laala'''
        if isinstance(value, tuple) and len(value) == 2:
            if (value[0], int) and isinstance(value[1], int):
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = value
                    return
        raise TypeError("position must be a tuple of 2 positive integers")
