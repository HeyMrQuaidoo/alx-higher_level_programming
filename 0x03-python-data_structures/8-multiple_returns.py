#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    sentence_first_elem = sentence[0] if length > 0 else None
    tup = length, sentence_first_elem
    return(tup)
