# How to define a function
```
def greet_person(name):
    '''
    This function is used to greet people
    '''
    print(f"Hello {name}")

greet_person('Jorge')
```
# Return
```
def multiply(num1, num2):
    '''

    '''
    total = num1 * num2
    return total

result = multiply(5, 10)
print(result)
```
# Dinamic functions
```
def check_3_figures(my_list):
    list_3_figures = []
    for n in my_list:
        if n in range(100, 1000):
            list_3_figures.append(n)
        else:
            pass
    return list_3_figures

result = check_3_figures([553, 992, 5674])
print(result)
```
# Example
```
coffee_prices = [('catppuccin', 1.5), ('express', 1.2), ('moka', 1.9)]

def most_expensive_coffee(coffee_prices):
    major_price = 0
    most_expensive_coffee = ''

    for coffee, price in coffee_prices:
        if price > major_price:
            major_price = price
            most_expensive_coffee = coffee
        else:
            pass

    return (most_expensive_coffee, major_price)

coffee, price = most_expensive_coffee(coffee_prices)

print(coffee, price)
```

# Function interaction
```
from random import shuffle

# Inital list
sticks = ['-', '--', '---', '----']

# Mix sticks
def mix(my_list):
    shuffle(my_list)
    return my_list

# Ask for a number
def try_your_luck():
    attempt = ''

    while attempt not in ['1', '2', '3','4']:
        attempt = input("Choice a number between 1 and 4: ")

    return int(attempt)

# Check attempt
def check_attempt(my_list, attempt):
    if my_list[attempt - 1] == '-':
        print("Let's wash the dishes")
    else:
        print("You are safe this time")

    print(f"You got number {my_list[attempt - 1]}")

mixed_sticks = mix(sticks)
the_choice = try_your_luck()
check_attempt(mixed_sticks, the_choice)
```
