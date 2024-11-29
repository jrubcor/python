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

# Enumerator
# Zip
# Random
