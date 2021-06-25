#Import random

#Create the function below:

def matrix_builder(integer):
    my_list = []
    for ele in range(integer): 
        my_list.append([])
        for elm in range(integer):
            my_list[ele].append(1)
    print(my_list)

matrix_builder(5)
        