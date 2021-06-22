
my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]


#your code go here:
hello = []

def count_on(a_list):
    for x in a_list:
        if type(x) is dict or type(x) is list:
            hello.append(x)

count_on(my_list)
print(hello)
