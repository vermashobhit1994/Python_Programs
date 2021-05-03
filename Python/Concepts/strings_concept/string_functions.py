#string functions in python

string = 'shobhitvermabestbest'

#1. First letter capital
print(string.capitalize())

#2. All letters to lowercase
teststr = 'SHOBHIT'
print(teststr.casefold())

#3.Center the string with leading spaces 
teststr = 'shobhit'
print(teststr.center(20))

#4. count the number of times substring occurs
print("e count = ",string.count('e'))
print("z count = ",string.count('z'))
print("e count = ",string.count('e',-8))#count the e from last 8 characters

#5.conver to binary string 
teststr = 'shobhit'
print(teststr.encode())#default encoding utf-8
teststr = "My name is Ståle"
#special character replacement
print(teststr.encode('ascii',errors = 'backslashreplace') )
print(teststr.encode('ascii',errors = 'ignore') )
print(teststr.encode('ascii',errors = 'namereplace') )
print(teststr.encode('ascii',errors = 'replace') )
print(teststr.encode('ascii',errors = 'xmlcharrefreplace') )





#6. checking if string endswith special substring
print(string.endswith('t'))
print(string.endswith('q'))
print(string.endswith('best'))#True

#7. replace the tabs by no of spaces
teststr = 's\th\to\tb\th\ti\tt'
print("original string ",teststr)
print(string.expandtabs(5))#replace by 5 spaces


#8. return the index of first occurence of string
print("v find at ",string.find('v'))
print("z find at ",string.find('z'))#return -1 if no string is found


#9. Return the index of last occurence of string
print("original string ",string) 
print("rfind ",string.rfind("best"))
print("rfind again",string.rfind('z'))#return -1 if string isn't found

#10. specify the input with parameter in string
teststr = 'shobhit'
print("Hello {0} with age = {1}".format(teststr,20))

#11. specify the input with key and value pair i.e dictionary
mydict = {'name':'shobhit','age':30}
print("Hello {name} with age = {age}".format_map(mydict))

#12. find the index of substring
print(string.index('t'))
try:
	print(string.index('z'))#ValueError if string isn't found
except ValueError as err:
	print("Error in finding index:",err)

#13. find the last occurence of substring 
print(string.rindex("best"))
try:
	print(string.rindex('z'))#gives ValueError if string isn't found
except ValueError as err:
	print(err)

#14. checking if alphanumeric characters	
print(string.isalnum())

#15. checking the alphabets characters
print(string.isalpha())

#16. checking the unicode decimal numbers
print(string.isdecimal())
teststr = '\u0033'
print("number check ",teststr.isdecimal())
teststr = '123'
print("number check again",teststr.isdecimal())


#17. checking if only digits
print(string.isdigit())
print("only digit test",teststr.isdigit())

#18. checking if string is identifier(only contain the a-z, A-Z,0-9,_)
print("identifier check",string.isidentifier())

#19. check lowercase of all letters
print(string.islower())
teststr = 'SHobhit'
print("islower check",teststr.islower())

#20. checking if character are numeric only
#Here exponent also numeric characters
print(string.isnumeric())
teststr = '1234'
print(teststr.isnumeric())
teststr = "-1"
print(teststr.isnumeric())
teststr = "\u00B2" #unicode for ²
print("exponent numeric check",teststr.isnumeric())
teststr = "\u0030" #unicode for 0
print("0 unicode numeric check ",teststr.isnumeric())


#21. check if all characters are non whitespace characters
print(string.isprintable())
teststr = "Hello!\rAre you #1?"
print("Whitespace string ",teststr.isprintable())

#22. check for all whitespace characters
print(string.isspace())
teststr = '\r\n'
print("isspace() ",teststr.isspace()) 

#23. check if all words start with Uppercase letter
print(string.istitle())
teststr = 'Hello World'
print("istitle",teststr.istitle())

#24. check if all letters are uppercase
print(string.isupper())
teststr = "SHOBHIT"
print("isupper",teststr.isupper())

#25. join string with iterable after the first value/character
teststr = "shobhit"
print("z".join(string))#here string specify the iterable and "z" is string to join
mylist = ['shobhit','apu']
print("good".join(mylist))

#26. left justify the string 
teststr = 'shobhit'
print(teststr.ljust(20),"good boy") #left justify by 20

#27. right justify the string
print(string.rjust(50),"string")

#28.convert the string to lowercase
teststr = "sHOBHIT"
print("lowercase string:",teststr.lower())

#29. remove the leading and ending spaces/characters
teststr = '****    shobhit   ****'
print(teststr.strip('* '))#here remove the leading and ending space and * character

#30. remove the leading spaces/characters
teststr = '***  shobhit  ***** '
print(teststr.lstrip('* '))#remove the leading space and  * character

#31. remove the ending spaces/characters
teststr = '***  shobhit  ***** '
print(teststr.rstrip('* '))#remove the leading space and  * character

#32. make a mapping table for replacement of string
print("original string :",string)
mapping_table_dict  = string.maketrans("best","good")#replace b -> g, e -> o, s -> o, t -> d
print(type(mapping_table_dict))

#33. Replace the character/string using the dictionary 
print(string.translate(mapping_table_dict))

#34. Parition the string by specified substring and return tuple of before, substring and after the substring
string = 'shobhit verma good best boy good hello good best'
print(string.partition('verma'))

#35.Paritition the string by finding the last occurence of substring and return the tuple of before,substring and after substring
print(string.rpartition('good'))


#36. replace substring by particular string
print(string.replace('good','hey',1))#replace only 1 time


#37. split the string into list based on substring
print("split() :",string.split('good'))#here substring gets removed

#38. split the string based on last 2 occurence of substring
print("rsplit():",string.rsplit('good',2))

#39. split the string into list based on '\n'
teststr = 'shobhit \nverma'
print(teststr.splitlines())

#40. return True if string startwith specified substring
teststr = 'shobhit verma'
print(teststr.startswith('shobhit'))
print(teststr.startswith('h'))#return False

#41. change all lowercase letters to uppercase and vice versa
print(string.swapcase())
teststr = 'sHoBhIt VeRMa'
print("swapcase():",teststr.swapcase())

#42. Return the string where every word starting character is uppercase rest are lower
print(string.title())

#43. change all letters to uppercase
teststr = 'shoBHIT VerMa'
print(teststr.upper())

#44. Fill all the starting spaces with zeroes and right justify the string
teststr = 'shobhit'
print(teststr.zfill(20))











