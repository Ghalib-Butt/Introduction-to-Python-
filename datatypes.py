# Python Datatypes
# 1. Text Type:	str
# 2. Numeric Types:	int, float, complex
# 3. Sequence Types:	list, tuple, range
# 4. Mapping Type:	dict
# 5. Set Types:	set, frozenset
# 6. Boolean Type:	bool
# 7. Binary Types:	bytes, bytearray, memoryview
# 8. None Type:	NoneType


# 1. String Practice
print("\n\n")
print("1. String Practice")
string = "My name is {} and I'm {} years old"
print(string.format('Ghalib', 25, 11))
string2 = " Ghalib Butt "
print(string2.upper())
print(string2.strip())
print(string2.replace('Ghalib', 'Ghalib Nawaz'))
print(string2.strip()[0:6])
string3 = "pakistan"
print(string3.capitalize())
string4 = "bananas, mangos, oranges"
print(string4.split(','))
print(string4.split(' '))


# 2. Numeric Practice
print("\n\n")
print("2. Numeric Practice")
a = 10
x = complex(1,7)
x2 = complex('2+14j')
print(type(a))
print(x, type(x))
print(x2, type(x2))
print(12E4, type(12E4))
print(12E4 / 100, type(12E4 / 100))
print(35e3, type(35e3))
print(35e3 / 100, type(35e3 / 100))


# 3. Sequence Practice
# In Python we have 4 built-in data types that are used as collection which includes
# Tuple, Set, List and Dictionay
print("\n\n")
print("3. Sequence Practice")
# List: Lists are used to store multiple items in a single variable. List items are ordered, changeable, and allow duplicate values.
listCreationWithListSyntax = list(('a', 'e', 'i', 'o', 'u'))
print(listCreationWithListSyntax)
myList = ['code', 'sleep', 'repeat']
print(myList, f'<length of list>: {len(myList)}', f'first value at 0 index: {myList[0]}')
print('First index value of first item in list: ', myList[0][0])
randomList = ['Ghalib Butt', 'male', 'Pakistan', 'PUCIT', 25, True]
print("Print randomList without first 2 items: ", randomList[2:])
print("Print randomList without last 2 items: ", randomList[:-2])
randomList[2] = "Lahore, Punjab, Pakistan."
print(type(randomList))
print(f'{randomList[1:4]} is a list: ', isinstance(randomList[1:4], list))
randomList.append('new item added at last')
randomList.insert(1, 'second item in List')
print(randomList)
# use of extend and other methods won't work in print statement e.g: print(randomList.extend(myList))
randomList.extend(myList)
randomList.extend(myList)
print(randomList)
randomList.remove('code')
randomList.pop(1)
randomList.pop()
myList.clear()
print("Current items in myList: ", myList)
del myList
print(randomList)
fruits = ('Apple', 'banana', 'Pineapple', 'Orange', 'Mango', 'Coconut', 'Cherry', 'Peach', 'Pomegranate')
largeNamedFruits = [fruit for fruit in fruits if len(fruit) >= 6]
largeNamedFruits.sort(reverse = True, key = str.upper)
print(largeNamedFruits)
largeNamedFruits.reverse()
print(largeNamedFruits)



# 6. Boolean Practice
# Values for False:- False, None, 0, "", (), [], {}
print("\n\n")
print("6. Boolean Practice")
print(bool(123))
print(bool("123"))
print(bool(''))
print(bool(["apple", "cherry", "banana"]))
print(isinstance(100, int))
print(10 > 100)
print(10 is 10)
print(10 is not 10)
print(10 in (1, 4, 7, 10))
print(10 not in [1, 4, 7, 10])


