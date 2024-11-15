# Print
This is a method who print a message onto the screen. Example:
`print("Hello world")`

To put quotation marks you can alternate single quotation marks with double quotation marks or viceversa
`print("Hello world, my name is 'Jorge'")`

The message can be a string, but also other object. But the object will be converted into a string before written to the screen
`print(150)` or `print(100+50)`

# Strings
Strings in python are surrounded by either single quotation marks, or double quotation marks
`print("hi guys")`

You also can write "\" and then put quotation marks
`print("Hello world, my name is \"Jorge\"")`

"\n" is for making a like break
`print('This is my first line\nThis is my second line')`

"\t" is an escape sequence that represents a tab character. When used within a string, int inserts a horizontal tab at that position
`print('Hello\tWorld')`

To assign a string to a variable:
`a = "Hello"`

You can also assign a multiline string to a variable by using three quotes:
```
a = """Lorem ipsum dolor sit amet,
consctetur adipiscing elit,
sed do eiusmod tempor incididunt""""
```

# Input
The input() function allows user input.
`input("What is your name my friend: ")`

You can put a input method into a print metho
`print(input("What is your last name my friend: "))`

A elaborate example
`print("Your name is: " + input("What is your name: ") + " " + input("What is your last name: "))`
