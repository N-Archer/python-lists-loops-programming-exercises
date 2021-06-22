chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']


def merge_list(list1, list2):
    #Your code go here:
    # new_list = []
    # for person in list1:
    #     new_list.append(person)
    # for person in list2:
    #     new_list.append(person)
    # return(new_list)
    return(list1 + list2)
    
print(merge_list(chunk_one, chunk_two))
