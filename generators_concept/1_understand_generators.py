#Program to understand generators in python i.e to generator one by one value
#from function.
#generator return an iterator 

#generator function due to use of yield
def topten():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

values = topten()
print(values)

print(values.__next__())
print(values.__next__())
print(next(values))

#print the remainig values i.e 4 and 5
for i in values:
    print(i)