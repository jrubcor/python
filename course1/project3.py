# Text analyzer

text = input("Enter a text: ")
text = text.lower()

a = input("Enter a letter: ")
b = input("Enter a letter: ")
c = input("Enter a letter: ")

# First
print(f"{a} appears {text.count(a)} times")
print(f"{b} appears {text.count(b)} times")
print(f"{c} appears {text.count(c)} times")

# Second
words = text.split()
print(f"Text has {len(words)} words words")

# Third
print(f"The first letter is: '{text[0]}' and the last is '{text[-1]}'")

# Fourth
words.reverse()
text = " ".join(words)
print(text)

# Fifth
answer = "python" in text
dict_answer = {True:'Yes, python is in text', False:'No, python is not in text'}
print(dict_answer[answer])
