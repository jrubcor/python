# Comparation operators
```
my_bool = 5>3
my_bool = 5<3
my_bool = 5>=3
my_bool = 5<=3
my_bool = 5==3
my_bool = 5!=3
my_bool = "hello world"!="hello satanas"
print(my_bool)
```
# Logic operators
```
my_bool = 4<5 and 3<7
my_bool = 4<5 or 3<7
print(my_bool)

text = "Hello this is my text"
my_bool = ('Hello' in text) or ('python' in text)
print(my_bool)

# Negation
my_bool = not 3<5
print(my_bool)
```
# Flow control
```
if 5 < 3:
    print("This is true")
elif 3 < 2:
    print("This is true")
else:
    print("None of the options were tru")
```
# Loops
For:
```
my_list = ['a', 'b', 'c', 'd']

for letter in my_list:
    print(letter)

my_list = ['pablo', 'laura', 'fede', 'luis', 'julia']

for name in my_list:
    if name.startswith('l'):
        print(name)

for object in [[1, 2], [3, 4], [5, 6]]:
    print(object)

for a, b in [[1, 2], [3, 4], [5, 6]]:
    print(a)
    print(b)

dic = {'k1':'a', 'k2':'b', 'k3':'c'}

for item in dic:
    print(item) # This prints keys

for item in dic.items():
    print(item) # This prints keys and values

for item in dic.values():
    print(item) # This prints keys

for a,b in dic.items():
    print(a, b) # This prints keys
```
While:
```
coins = 5

while coins > 0:
    print(f"I have {coins} coins")
    coins -= 1
else:
    print(f"I don't have more money")

answer = 's'

while answer == 's':
    answer = input("s/n: ")
else:
    print("bye")
```
# Range
```
for element in range(0, 10):
    print(element)

print("----")
for element in range(0, 10, 2):
    print(element)

my_list = list(1, 101)
print(my_list)
```
# Enumerator
```
my_list = ['a', 'b', 'c']
index = 0
for element in my_list:
    print(index, element)
    index += 1

my_list = ['a', 'b', 'c']
for element in enumerate(my_list):
    print(element) # element = Tuple

my_tuples = list(enumerate(my_list))
print(my_tuples)
```
# Zip
```
names = ['Ana', 'Hugo', 'Valeria']
ages = [65, 29, 42]
cities = ['Lima', 'Madrid', 'Mexico']

combined = zip(names, ages) # >>> zip object
combined = list(zip(names, ages, cities))
print(combined)

for name, age, city in combined:
    print(f"{name} is {age} and lives in {city}")
```
# Min and Max
```
minor = min(58,96,72,64,35)
major = max(58,96,72,64,35)
print(minor)
print(major)

my_list = [58,96,72,64,35]

print(f"Minor is {min(my_list)} and major is {max(my_list)}")

names = ["Jorge", "Alberto", "Steph"]

print(min(names))

dic = {'C1':45, 'C2':11}
print(min(dic)) # Get the minor key
print(min(dic.values())) # Now Get the minor value
```
# Random
```
from random import *

# Randint
ran = randint(1, 50) # Random integer number
print(ran)

# Uniform
ran = uniform(1, 5) # Random decimal number
ran = round(uniform(1, 5), 1) # Random decimal number (1 decimal)
print(ran)

# Random
number = random()
print(number)

# Choice
colors = ['blue', 'red', 'green', 'yellow']
ran = choice(colors)
print(ran)

# Shuffle
numbers = list(range(5, 51, 5))
shuffle(numbers)
print(numbers)
```
# List comprehensions
```
word = 'python'

my_list = []

for letter in word:
    my_list.append(letter)

print(my_list)

# This is another way to create a list without use loops

word = 'python'
my_list = [letter for letter in word]

print(my_list)

my_list = [n for n in range(0,21)]
print(my_list)

# n/2
my_list = [n/2 for n in range(0,21)]
print(my_list)

# If
my_list = [n for n in range(0,21) if n*2 > 10]
print(my_list)

# If/else
my_list = [n  if n*2 > 10 else 'no' for n in range(0,21)]
print(my_list)

feet = [10, 20, 30, 40, 50]
meters = [f / 3.281 for f in feet]
print(meters)
```
# Match
```
serie = "N-02"

match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("That product doesn't exist")
```
