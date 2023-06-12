#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence != '':
        initial = sentence[0]
    else:
        initial = None
    return (len(sentence), initial)
