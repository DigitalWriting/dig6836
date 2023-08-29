import pyperclip, random

# copy the data from the clipboard into a variable called text
text = pyperclip.paste()

# split the data into a new list variable so that each element is divided by a newline
# note that the backslash n represents a new line in Python
text2 = text.split("\n")

# randomly shuffle the order of the list elements in the text2 list
random.shuffle(text2)

# as long as the length of the text 2 list is greater than zero (meaning, there is still stuff in it)
while len(text2) > 0:
    item = text2.pop() # popping an item from a list retrieves it and removes it from the list
    print(item) # print out whatvever you just popped off the list 
