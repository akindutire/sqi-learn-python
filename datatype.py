# line commenting
# print('Hello world')

# block commenting
"""
    A lot of comment in multiple lines
    another line
"""
perosn = "!John doe@"
print(perosn.strip('!'))

"""
var2 = input("Asking for input: ")
print(var2)

if var2 == "great":
    print("You are cool")
"""

# Strings
text1 = "I am akindutire ayomide"
# string lenght
print(len(text1))

#text indexing
print(text1[0]) # first character
print(text1[-1]) # last character
print(text1[1:5]) #picks from index 1 until 4
print(text1.upper())
print(text1.lower())
print(text1.replace('d', 'Y'))
print(text1.split('a'))
# capitalise first letter only
print(text1.capitalize())
# capitalise every first letter of each word
print(text1.title())


# Sequence datatypes, - List, Tuple, Range

# They are not mutable, in nlp words must be changed and dataset is often read as tuple
studentTuple = "John", 25, "A"
print("A tuple", studentTuple)

anotherStudentTuple = ("John", 25, "A")
print("Another Student Tuple representation", anotherStudentTuple)

# it can also be sliced
anotherStudentTuple2 = ("John", 'Erik', 25, "A")
print("A sliced tuple", anotherStudentTuple2[0:3])

#Unpacking a tuple, similar to list(a,s,d) = [3,34,2] in php, the *rest would capture item of the iterable till the last or the item before the last if an extra var 
# is added after the *rest, e.g f,s,*rest,last_item
first_var, second_var, *rest = anotherStudentTuple2
print("Remaining of the tuple", rest)



# They are mutable
studentList = ["John", 25, "A"]
print("A list", studentList)
print("A Sliced list", studentList[0:2])
print("Append to a list", studentList.append("New value2"))
print("Extend a list", studentList.extend(["Value3", "Value4"]))
studentList.insert(1, "Inserted value at index 1")
print("INSERT INTO A ARRRAY A INDEX 1", studentList)

# steps in reversal of a list
print("Reversing a list", studentList[::-1])

studentList.pop()
print("Popping an item from a list", studentList)

studentList.remove(25)
print("Remove an item from a list", studentList)

# Clear a list
studentList.clear()
print("Cleared list", studentList)

# Basically used to define numbers, range(start, end, step)
rangeOfTwentyItems = range(20)
print("Range of values appearing as list", list(rangeOfTwentyItems))

multiVar, y, z = 5 + 5, "John", 25.5
print("Concurrent var assignment, getting one of the values of var Y:", y)

concatenatedString = "I am " + studentTuple[0] + " and I am " + str(studentTuple[1]) + " years old."
print("Unformatted mode of concat, ", concatenatedString)

# formatted string
# age = input("What is your age? ")
# formattedString = f"I am {studentList[0]} and I am {age} years old.\n"

# # multiply the formatted string 10 times
# formattedString = formattedString * 10
# print(formattedString)

# join arrays and implode them
print(",".join(['a','b']+['c','d']))

# Quick one: generate list out of range via list function, you can get type using type function
# Mapping datatype
# - Dictionary -  Similar to objects in JS, it is ordered
firstDict = {
    'key1' : 'Value1',
    'key2': 'Value2',
    'key3': 'Value3'
}
print('All keys of first dict', firstDict.keys()) # print keys in a dict
print('All values of first dict', firstDict.values()) # print values in a dict
print('Remove item from a dict', firstDict.pop('key3'))
print('Update dict', firstDict.update({'key4': 'v', 'key5': 'v16'}))
firstDict["key1"] = 'Value1AndAmmended'
print("Grid bracket can be used to access dict value too, grid throws key error if value doesn't exist", firstDict)
print("using .get will access value by key too and won't throw error if key doesnt exists")
print('Dump the full dict', firstDict.items())
print('Using the dict function to create a dictionary', dict(f=1,g=2))
print('You can iterate using for loop which basically index keys')
for key in firstDict:
    print("Each key in first dict")
    
print("Key and value of dict is accessed via items fn and its loop can be written as double iter")
for k,v in firstDict.items():
    print(f"Key: {k}, Value: {v}")
# - Set, it is used to add unique items and unordered
firstSet = {'A', 'B', 'b', 'a', 'A'} 
print('First normal set', firstSet)
firstSet.add("F") 
# same way .remove can be used to pop items, consequently .clear can take out all items, 
# a major diff btw .remove and .discard is, the remove fx throws a key error is if item is not in a silent but discard doesn't and both does same job if element is present
firstSet.discard("G")
print('Add a single F to set', firstSet)
firstSet.update(['D',3])
print('More items added', firstSet)

secondSet = {'A', 'G', 'l'}
print("Union", firstSet.union(secondSet)) 
print("Intersection", firstSet.intersection(secondSet)) 
print("Difference", firstSet.difference(secondSet)) 
print("Symmetric Difference", firstSet.symmetric_difference(secondSet)) 

print("Super set", firstSet.issuperset(secondSet)) 
print("Sub set", firstSet.issubset(secondSet)) 
print("Disjoint", firstSet.isdisjoint(secondSet)) 


# - FrozenSet - while set is a major mapping datatype, they are still mutable, to turn them to immutable, we can use the fronzenSet function
firstFrozenSet = frozenset(firstSet)
print("First frozen set", firstFrozenSet)

# - BINARY TYPES (bytes, bytearray, memoryview)
# - Bytes , the iterables in bytes function is the ascii codes which are basically byte, however bytes is immutable
firstBytes = bytes([68,78,10,11])
print(firstBytes)

# Individual byte can be mutable tho
firstByteArray = bytearray([68,78,10,11])
firstByteArray[1] = 70
print(firstByteArray)

# Get ascii/unicode of a char or char of an ascii code
print("ASCII or Unicode of character A", ord('A')) 

print("Character at Unicode/ascii of 65", chr(65)) 

# Memory view - , memory view aren't directly mutable, it points us to where a byte is located in the memory
# consider its mutablility based on the datastructure it is pointing, it is basically a pointer
byteObjectToCrossRef = bytearray([89, 76])
firstMemoryView = memoryview(byteObjectToCrossRef)
firstMemoryView[1] = 65
print(firstMemoryView)


# Quick one: None is also a datatype
# Qucik two:  any is also a dataype


# Array, it is best for representing large multidemensional data
firstArray = [ [1,2,3,4,5] , [6,7,8,9,10] ]
print("First array", firstArray)