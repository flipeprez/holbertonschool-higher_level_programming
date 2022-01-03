#!/usr/bin/python3
def multiple_returns(sentence):
    largo = len(sentence)
    if largo == 0:
        sentence[0] = None
        return (largo, None)
    return (largo, sentence[0])
