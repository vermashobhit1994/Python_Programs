#program to understand how to access string via the single line


#add all items with letter a in it

names = ['shyam','ram','apu','shobhit']

newlist = []


for item in names:
	if 'a' in item:
		newlist.append(item)
		
print(newlist)

print("After list comprehension")
#list comprehension -> create new list based on values of old list
#Here the item is expression ,names is iterable data, if is condition 
mylist = [ item for item in names if 'a' in item ] 
print(mylist)

#Here the expression can be manipulated
#put the items in list after converting to uppercase
mylist = [item.upper() for item in names if 'a' in item]
print(mylist)

#Here the expressin can also contain the condition
#Here the element if 'ram' then add 'khoyam' instead of 'ram'
mylist = [item if item != 'ram' else 'khoyam' for item in names]
print(mylist)



