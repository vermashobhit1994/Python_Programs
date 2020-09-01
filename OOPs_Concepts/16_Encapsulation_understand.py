#Program to understand Encapsulation in python
#it is done by __varName .
class Computer:

    def __init__(self):
        #__maxprice is private member and can only be accessed inside the class
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

#Create an object of Computer class
c = Computer()

print("\n\n")

#print the current maxprice 
print("Current max price is ")
c.sell()

print("\n\n")

# change the price.
#__maxprice isn't changed since it is a private member
print("Changing the max price")
c.__maxprice = 1000
c.sell()

print("\n\n")

#Here since __maxprice is private member so we need to use setter function to 
#change the value. 
c.setMaxPrice(1000)
c.sell()