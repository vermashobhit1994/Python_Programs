
#These are ordered, duplicate allowed, unchangeable(immutable)

###############################################################################################################################################################
#create tuple/ Packing a tuple 

#a) for single element
mytuple = (1,)#create a tuple with only one element . Here , is necessary. If not put then change according to data type
mynewtuple = tuple( (10,))
print(mytuple,type(mytuple))
print(mynewtuple, type(mynewtuple))

#b) for multiple elements
mynewtuple = (1,2,5,8)
mytuple = tuple( (1, 'shobhit',1.5))
print("create using constructor ",mytuple,mynewtuple)

##############################################################################################################################################################


##############################################################################################################################################################
#change element of the tuple
templist = list(mynewtuple)
templist[3] = 45  #changing the 4th element
mynewtuple = tuple(templist)#copy the elements from templist to mynewtuple after changing it to tuple
print("after changing the 4th element ",templist)

##############################################################################################################################################################



##############################################################################################################################################################
#adding element to tuple

mynewtuple += (78,)
print("After adding  ",mynewtuple)

#by changing to list
templist = list(mynewtuple )
templist.append(452)
mynewtuple = tuple(templist)
print("after adding new element ",mynewtuple) 

##############################################################################################################################################################

##############################################################################################################################################################
#unpack tuple
mytuple = (1,2,3)
a,b,c = mytuple	
print("unpack without *: ",a,b,c)

#if collect more than 1 element in single variable
#Here * causes to collect element as a list
newtuple = (12,13,14,78,569)
a,*b,c = newtuple
print("unpack using *: ",a,b,c)
##############################################################################################################################################################

##############################################################################################################################################################
#loop through tuple

#using for loop
for element in newtuple:
	print("Element : ",element)
	
#using index number
for i in range ( len(newtuple) ):
	print("newtuple[{}] = {}".format(i, newtuple[i]) )

##############################################################################################################################################################


##############################################################################################################################################################
#join two tuples
tuple1 = (1,2,3,3,3)#Here duplicate elements are allowed
tuple2 = (4,5,6)
print(tuple1+tuple2)

#make the element repeat number of times 
print(tuple2 * 2)
##############################################################################################################################################################

##############################################################################################################################################################
#tuple functions 

#1. find the length of tuple
print("len(tuple1) ",len(tuple1))

#2. count the element occurence
print("cnt 3 = ",tuple1.count(3))
print("cnt 500 = ",tuple1.count(500)) #if element isn't found then return 0

#3. find the first occurence index of element
print("index ",tuple1.index(3))
#print(tuple1.index(12))#ValueError if element isn't found
##############################################################################################################################################################

##############################################################################################################################################################
#delete the tuple
del tuple1
#print(tuple1) #NameError if try to print it
##############################################################################################################################################################

