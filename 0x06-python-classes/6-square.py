#!/usr/bin/python3
    '''lala'''


class Square:
    '''lala'''
    def __init__(self, size=0, position=(0, 0)):
        '''lala'''
	    if type(size) is not int:
		raise TypeError("size must be an integer")
	    elif size < 0:
		raise ValueError("size must be >= 0")
	    else:
		self.__size = size

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
	elif self.__size > 0:
	    for a in range(0, self.__size):
		for h in range(0, self.__size):
		    print("#", end="")
		print()
        
    @property
    def position(self):
        '''lalal'''
        return self.__position
        
    @position.setter
    def position(self, value):
        '''laala'''
        raise TypeError("position must be a tuple of 2 positive intergers")

    def my_print(self):
        '''lalala'''
        if self.__size == 0:
            print()
            return

