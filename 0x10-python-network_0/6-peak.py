# !/usr/bin/python3

def find_peak(list_of_integers):
    max = 0
    for i in list_of_integers:
        if i > max:
            max = i
        elif list_of_integers == ():
            return None
    return max
