#!/usr/bin/python3
def uppercase(str):
    for hp in str:
        hp = ord(hp)
        if hp > 96 and hp < 123:
            hp = hp - 32
        print("{:c}".format(hp), end="")
    print()
