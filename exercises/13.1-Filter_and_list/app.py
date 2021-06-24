
all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

#Your code go here:

def filter_list(rnames):
    return rnames[0] == "R"

resulting_names = list(filter(filter_list, all_names))

print(resulting_names)




