# Data type
- string(str) `"Hello world"`
- number:
    - integer(int) `5`
    - floating(float) `5.2`
- lists(list) `["salt"], 1, -3, 4.5, "marte"]`
- dictionaries(dict) `{'color':'red', 'art','music'}`
- tuples(tuple) `('mon', 'tue', 'wed', 'thu', 'fri', 'saturday', 'sunday')`
- sets(set) `{'a', 'b', 'c', 'd', 'e'}`
- booleanos(bool) `True, False`

# Variables
You can assign strings to variables:
```
name = "Jorge Oziel"
print(name)
print(type(name))
```

You can assign numbers:
```
number_a = 12
number_b = 5
print(number_a+number_b)
```

How to save information entered by de user in variables:
`a = input("Enter your name: ")`

# Rules for variable names
1. legible: must be consistent `dog_name = "terry"`
2. unit: should not have spaces, you can separate words using _ `my_name = "Jorge"`
3. not hispanisms, for example: instead of año use anio
4. You can use numbers, but not at the beginning
5. you can't use signs
6. you can't use keywords like print, input, string, and that kind of words.

# Casting
The process of transform a type of data to a other type is called casting, there are two types of casting:
1. implicit: 
Python converts the data type to another data type automatically. In this process, the user does not need to do anyhing. For example:
```
num1 = 20 # this variable is integer
num2 = 30.5

num1 = num1 + num2 # now num1 will be converted to float

print(num1) # >>> 50.5
print(type(num1)) # >>> <class 'float'>
print(type(num2)) # >>> <class 'float'>
```
2. explicit
Python needs that user does something to converts a data type to another. For example:
```
num1 = 5.8
print(num1)
print(type(num1))

num2 = int(num1) # Here's the casting, we converted a float to an integer
print(num2) # >>> 5
print(type(num2)) # >>> int <class 'int'>
```

# Format strings
There are several ways to format strings:
1. Using function format():
```
color_auto = "red"
license_plate = "ZAC1921HB"
print("My car is {} and has the license plate {}".format(color_auto, license_plate))
```
2. Using literal strings:
```
color_auto = "red"
license_plate = "ZAC1921HB"
print(f"My car is {color_auto} and has the license plate {license_plate}")
```

# Mathematic operations
```
x = 6
y = 2
z = 7
```
1. Addition
`print(f"{x} plus {y} equals {x+y}")`
2. Substraction
`print(f"{x} minus {y} equals {x-y}")`
3. Multiplication
`print(f"{x} times {y} equals {x*y}")`
4. Division
`print(f"{x} divided {y} equals {x/y}")`

4.1 Floor division: It is a mathematical operation that divides two numbers and rounds the result down to the nearest integer. For example:
`print"The floor division of {z} by {y} is {z//y}")`

5. Modulo
This operation finds the remainder after division of one number by another
`print(f"{z} modulo {y} is {z%y}")`

6. Power
`print(f"{x} raised to the power of {y} is {x**y}")`

7. Root
`print(f"The square root of {x} is {x**0.5}")`

# Rounding
This function returns a floating point number that is a rounder version of the specified number, with the specified number of decimals. round(number, digits)
`print(round(90/7,2))`
