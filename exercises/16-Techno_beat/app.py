
def lyrics_generator(my_list):
    string=""
    count = 0
    for i in range(len(my_list)):
        if my_list[i] == 0:
            string += " Boom "
        elif my_list[i] == 1:
            string += " Drop the base "
            count += 1
        if count == 3:
            string += " !!!Break the base!!! "
    return string
        



# Your code go above, nothing to change after this line:
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))