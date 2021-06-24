par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}
#your code go here:
def counting(char):
    if char != " ":
        if char in counts: 
            counts[char] += 1
        else:
            counts[char] = 1
    return counts
    
list(map(counting, par.lower()))

print(counts)

