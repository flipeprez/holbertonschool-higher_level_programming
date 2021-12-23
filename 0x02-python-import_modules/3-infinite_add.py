#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    number = 0
    for i in range(1, len(sys.argv)):
        number = number + int(sys.argv[i])
print(number)
