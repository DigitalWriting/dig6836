import pyperclip, random

# copy the data from the clipboard into a variable called text
text = pyperclip.paste()

# split the data into a new list variable so that each element is divided by a newline
# note that the backslash n represents a new line in Python
words = text.split("\n")

# randomly shuffle the order of the list elements in the text2 list
random.shuffle(words)

# loop through the new, shuffled version of words and print out every line to the console
for word in words:
    print(word)   
    
