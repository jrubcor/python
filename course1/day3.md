# String methods

# Index
This is useful to:
1. Know the index of a character
```
# Text analyzer
my_text = "This is a text"

result = my_text[-1]
print(result)
```

2. Know the character in an determineted index
```
# Text analyzer
my_text = "This is a text"

character = my_text.index('text')
print(character)

character = my_text.index('text',5)
print(character)

character = my_text.rindex('a')
print(character)
```

# Slicing
This is used to extract characters from a string
```my_text = "ABCDEFGHIJLM"
print(my_text)

# Slicing
substring = my_text[5:7]
print(substring)

substring = my_text[0:7]
print(substring)

substring = my_text[0:10:2]
print(substring)
```

# Methods
- Upper
```
text = "This is the Jorge's text"

result = text.upper()
print(result)
result = text[5].upper()
print(result)
```

- Lower
```
text = "This is the Jorge's text"

result = text.lower()
print(result)
```

- Split
```
text = "This is the Jorge's text"

result = text.split()
print(result)
result = text.split("i")
print(result)
```

- Join
```
text = "This is the Jorge's text"

a = "Learn"
b = "Python"
c = "is"
d = "awesome"
e = " ".join([a, b, c, d])
e = "-".join([a, b, c, d])
print(e)
```

- find
```
text = "This is the Jorge's text"
nd
result = text.find("z")
print(result)
```

- replace
```
text = "This is the Jorge's text"

result = text.replace("Jorge","Sofia")
print(result)
```

# Properties
- Immutable
```
name = "Jorge"
name[0] = 's'
# >>> Error
```

- Concatenable
```
name = "Jorge"
last = "Rubio"
print(name + " " + last)
# >>> Jorge Rubio
```

- Multiplicable
```
name = "Jorge"
names= name*5
print(names)
# >>> JorgeJorgeJorgeJorgeJorge
```

- Multiline
```
name = """Jorge
Rubio"""
print(name)
```

- Check substrings into strings
```
text = """A thousand small white fish
as if the color of the
wates was boiling
"""
print("thousand" in text)
print("thousand" not in text)
```

- Calculate length
```
text = """A thousand small white fish
as if the color of the
wates was boiling
"""
print(len(text))
```

# Lists
```
my_list = ['a', 'b', 'c']
print(type(my_list))
```

# Size
```
size = len(my_list)
print(size)
```

# Slicing
```
sublist = my_list[0:2]
print(sublist)
```

# Concatenate
```
my_list2 = ['d', 'e', 'f']
my_list3 = my_list + my_list2
print(my_list3)
```

# Mutable
```
my_list3[0] = 'z'
print(my_list3)
```

# Methods
```
my_list3.append('g')
print(my_list3)
my_list3.pop() # This eliminates the last element
print(my_list3)

eliminated = my_list3.pop(2) # This eliminates the element in the index 2
print(my_list3)
print(eliminated)

my_list4 = ['g', 'o', 'b', 'm', 'c']
my_list4.sort()
print(my_list4)

my_list4.reverse()
print(my_list4)
```

# Dictionaries
```
dictionary = {'c1':'value1', 'c2':'value2'}
print(type(dictionary))
print(dictionary)

# Get a value
a = dictionary['c1']
print(a)

client = {'name':'Juan', 'last_name':'Fuentes','weight':'88', 'size':'166'}
query = (client['last_name'])
print(query)

dic = {'c1':55, 'c2':[10,20,30], 'c3':{'s1':100, 's2':200}}
print(dic['c2'][1])
print(type(dic['c3']))
print(dic['c3']['s2'])

dic = {'c1':['a', 'b', 'c'], 'c2':['d', 'e', 'f']}
print(dic['c1'][0].upper())

# How to add elements
dic = {1:'a', 2:'b'}
print(dic)

dic[3] = 'c'
print(dic)

dic[2] = 'B'
print(dic)

print(dic.keys())
print(dic.values())
print(dic.items())
```

# Tuples
Tuples are more efficient and immutables
```
my_tuple = (1,2,3,4)
t = (1, 5.6, 'hello', {'1':'23'})

# Acess an element of a tuple
print(my_tuple[2])

# Immutable 
# my_tuple[0] = 2 # (this is not possible)

# Casting
my_arrange = list(my_tuple)
print(my_arrange)

# Assignment
t = (1, 2, 3)
x, y, z = t
print(x, y, z)

print(len(t))
 
# Methods
print(t.count(1)) # Count items
print(t.index(1)) # Search items
```

# Sets

-They don't have index
-Not accept lists and dictionaries
-Immutables
-Not duplicate
```
my_set = set((1, 2, 3, 4))
my_set = {1, 2, 3, 4}
my_set = {1, 2, 3, 4, 4, 2, 1} # Duplicates will be removed

print(my_set)
# print(my_set[0]) # This is wrong
# my_set[0] = 3 # This is wrong

# Methods
# Length
print(len(my_set))

# Queries
print(2 in my_set)

s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)
print(s3)

s1.add(4)

s1.remove(3)
s1.remove(7) # Error because 7 is not into s3

s1.discard(3) # Discard the element 3 (if it not exists there is not problem)


s1.pop() # Remove a random element
```

# Booleans


```
my_bool = 3 > 2
my_bool = bool(3 > 2)
my_bool = bool() # This will be False
my_list = [1, 2, 3, 4]
my_bool = 5 in my_list
print(my_bool)
```
