mylist = [12,'shobhit',45.12,12,'shobhit']

#1. adding item to end of list
mylist.append('apu')
print(mylist)

#2. copy the list items
copylist = mylist.copy()
print("copylist",copylist)
print("original list",mylist)

#3. count the number of elements with element specified
print(mylist.count('a')) #0 return if no element found
print(mylist.count(12))

#4. to add another list to an already existing list
#   to add more than one item to an already existing list
mylist.extend( [10,11,12])
print(mylist)

print("before adding mylist")
print(copylist)

print("After adding mylist")
copylist.extend(mylist)
print(copylist)

#5. return the first occurence index of element
print(copylist.index('shobhit'))
#print(copylist.index('z'))  #ValueError if element isn't found

#6. insert a one item at specified index only
mylist.insert(3,100)
print(mylist)


#7. Return the Deleted element at specified index
print(mylist.pop(3))
print(mylist)
#print(mylist.pop(100))#IndexError if item index isn't exist 

#8. To remove first occurence of item by specify its name
print(mylist.remove('shobhit'))
print(mylist)
#print(mylist.remove('ver')) #ValueError if item isn't exists in list

#9. Revese the string
mylist.reverse()
print(mylist)

#10. Sort the list ascending order(default case), descending order or based on function specified
templist = ['shobhitverma','apukhote','laptop','guitar']

templist.sort()
print(templist)

templist.sort(reverse=True)#sort the list in descending order
print(templist)

#reversed based on external function
def myfunc(element):
	return len(element)

templist.sort(reverse=True,key=myfunc)#sort the string based on length of string and reverse it.
print(templist)


#11. Removes all elements from list
mylist.clear()
print(mylist)
copylist.clear()
print(copylist)

del mylist
print(mylist)#NameError occurs since mylist is deleted

















