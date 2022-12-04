#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    for i in range(len(my_list)):
            if my_list[i] % 2 == 0:
        return (my_list[i], True)
            else:
        return (my_list[i], False)
                
