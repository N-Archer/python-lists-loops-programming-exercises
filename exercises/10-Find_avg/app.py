my_list = [2323,4344,2325,324413,21234,24531,2123,42234,544,456,345,42,5445,23,5656,423]

#Your code here:
def average(a_list):
    total = 0 
    for i in a_list:
        total += i
    avg = total / len(a_list)
    return avg

print(average(my_list))



