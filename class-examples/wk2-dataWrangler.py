import pyperclip, string, random

contents = "" # holds clipboard contents
keeprunning = True # boolean to keep program running 

def showMenu():
    print("1: Get and display new clipboard contents.")
    print("2: Lowercase clipboard contents.")
    print("3: Reverse clipboard contents.")
    print("4: Count words in clipboard contents.")
    print("5: Randomize cliboard contents.")
    print("6: Search for word in text.")
    print("0: Exit program.")

while (keeprunning):
    showMenu()
    action = input("Command: ")
    if (action == "0"):
        keeprunning = False
        print("Goodbye!")
    elif (action == "1"):
        contents = pyperclip.paste()
        print(contents)
    elif (action == "2"):
        print(contents.lower())
    elif (action == "3"):
        print(contents[::-1])
    elif (action == "4"):
        words = contents.split()
        num_words = len(words)
        print("Words: " + (str)(num_words))
    elif (action == "5"):
        words = contents.split()
        random.shuffle(words)
        contents = " ".join(words) # turn the list of words into a string, with spaces in between
        print(contents)
    elif (action == "6"):
        query = input("Enter search query: ")
        words = contents.split()
        matches = words.count(query)
        print(f"This word appears {matches} times in the text.")
    else:
        print("Input not understood. Please type a number as shown above.")
    
    
