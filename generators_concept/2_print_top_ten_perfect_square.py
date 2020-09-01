#program to print the 1 to 10 perfect squares using the generator function
def print_squares():
    n = 1#initialize the n value
    while n <= 10:
        print("Before yield")
        yield n *n
        n += 1#increment the n value
        print("After increment\n\n")

values = print_squares()
for i in values:
    print(i)#print the value when yield is called
    