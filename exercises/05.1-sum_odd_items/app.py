arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:


def sum_odds(my_list):
    total = 0
    for num in my_list:
        if int(num) % 2 != 0:
            total += int(num)
    return(total)    
    
print(sum_odds(arr))

