my_list = [43,23,6,87,43,1,4,6,3,67,8,3445,3,7,5435,63,346,3,456,734,6,34]


#Your code go from here:

def biggest_int(a_list):
    biggest = 0
    for i in a_list:
        if i > biggest:
            biggest = i
    return biggest

print(biggest_int(my_list))



