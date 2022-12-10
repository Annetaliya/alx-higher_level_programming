#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return (0)
    add = 0
    avg = 0
    for i in my_list:
        avg += (i[0] * i[1])
        add += i[1]
    return (avg / add)
