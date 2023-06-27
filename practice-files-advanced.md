# File Operations Practice Problems (Advanced)

Here are ten Python practice exercises for working with basic file management operations.

**Exercise 1: Mad Libs Generator**

Create a program that reads a template file containing placeholders (e.g., `<noun>`, `<verb>`) and prompts the user to enter specific words for each placeholder. The program should then generate a new file with the placeholders replaced by the user's input.

Sample code:

```python
template_file = "template.txt"
output_file = "output.txt"

# Read the template file
with open(template_file, "r") as file:
    template = file.read()

# Prompt the user for inputs
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")

# Replace placeholders with user inputs
output = template.replace("<noun>", noun).replace("<verb>", verb)

# Write the output to a new file
with open(output_file, "w") as file:
    file.write(output)
```

**Exercise 2: Secret Diary**

Write a program that simulates a secret diary. The program should prompt the user for a password and only allow access to the diary if the correct password is entered. If the password is correct, the program should display the diary's contents. Otherwise, it should display an error message.

Sample code:

```python
diary_file = "diary.txt"
password = "mysecretpassword"

entered_password = input("Enter the password: ")

if entered_password == password:
    with open(diary_file, "r") as file:
        contents = file.read()
    print(contents)
else:
    print("Incorrect password. Access denied.")
```

**Exercise 3: File Analyzer**

Write a program that reads a text file and analyzes its content. The program should count the number of words, sentences, and paragraphs in the file. It should also calculate the average word length and display the most common words used.

Sample code:

```python
file_name = "text.txt"

with open(file_name, "r") as file:
    contents = file.read()

# Counting words, sentences, and paragraphs
words = contents.split()
sentences = contents.count(".") + contents.count("?") + contents.count("!")
paragraphs = contents.count("\n\n") + 1

# Calculating average word length
total_length = sum(len(word) for word in words)
average_length = total_length / len(words)

# Displaying analysis results
print("Analysis results:")
print("Number of words:", len(words))
print("Number of sentences:", sentences)
print("Number of paragraphs:", paragraphs)
print("Average word length:", average_length)
```

**Exercise 4: Data Backup**

Create a program that takes a backup of a specified file. The program should ask the user for the name of the file to be backed up and create a new file with the same content but a different name (e.g., appending "_backup" to the original filename).

Sample code:

```python
import shutil

file_to_backup = input("Enter the filename to backup: ")
backup_file = file_to_backup + "_backup"

shutil.copyfile(file_to_backup, backup_file)
print("Backup created:", backup_file)
```

**Exercise 5: Playlist Generator**

Write a program that generates a playlist based on a user's music preferences. The program should read a file containing a list of songs, each on a separate line. It should then prompt the user to enter their favorite genre and generate a playlist containing songs from that genre.

Sample code:

```python
playlist_file = "songs.txt"
genre = input("Enter your favorite genre: ")

with open(playlist_file, "r") as file:
    songs = file.readlines()

playlist

 = [song.strip() for song in songs if genre.lower() in song.lower()]

print("Your", genre, "playlist:")
for song in playlist:
    print(song)
```

**Exercise 6: Code Organizer**

Create a program that organizes a directory containing code files. The program should ask the user for a directory path and then categorize the files based on their file extension. It should create subdirectories for each file extension and move the corresponding files into their respective directories.

Sample code:

```python
import os
import shutil

directory = input("Enter the directory path: ")

for file_name in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, file_name)):
        file_extension = os.path.splitext(file_name)[1][1:]  # Extracting the file extension
        
        # Creating a subdirectory for each file extension if it doesn't exist
        if not os.path.exists(os.path.join(directory, file_extension)):
            os.makedirs(os.path.join(directory, file_extension))
        
        # Moving the file to its corresponding subdirectory
        shutil.move(os.path.join(directory, file_name), os.path.join(directory, file_extension, file_name))
        
print("Files organized successfully!")
```

**Exercise 7: File Encryption**

Write a program that encrypts a text file using a simple substitution cipher. The program should prompt the user for the name of the file to be encrypted and generate a new encrypted file. Each character in the original file should be replaced with a corresponding character from a predefined mapping.

Sample code:

```python
original_file = input("Enter the name of the file to encrypt: ")
encrypted_file = "encrypted.txt"
mapping = {
    "a": "x",
    "b": "y",
    "c": "z",
    # ... add more mappings as needed
}

with open(original_file, "r") as file:
    original_text = file.read()

encrypted_text = "".join(mapping.get(char.lower(), char) for char in original_text)

with open(encrypted_file, "w") as file:
    file.write(encrypted_text)

print("File encrypted successfully!")
```

**Exercise 8: File Compression**

Create a program that compresses a text file using a basic compression algorithm. The program should read the file, identify repeated sequences of characters, and replace them with shorter representations. It should then generate a new compressed file with the updated content.

Sample code:

```python
file_to_compress = input("Enter the filename to compress: ")
compressed_file = "compressed.txt"

with open(file_to_compress, "r") as file:
    original_text = file.read()

compressed_text = ""
current_char = original_text[0]
count = 1

for char in original_text[1:]:
    if char == current_char:
        count += 1
    else:
        compressed_text += current_char + str(count)
        current_char = char
        count = 1

compressed_text += current_char + str(count)

with open(compressed_file, "w") as file:
    file.write(compressed_text)

print("File compressed successfully!")
```

**Exercise 9: File Renamer**

Write a program that renames a batch of files in a directory. The program should prompt the user for a directory path and a new filename pattern. It should then rename all the files in the directory based on the pattern, using a numeric sequence for each file.

Sample code:

```python
import os

directory = input("Enter the directory path: ")
filename_pattern = input("Enter the new filename pattern: ")

file_list = os.listdir(directory)
file_list.sort()  # Sorting the files for consistent renaming order

for i, file_name in enumerate(file_list):
    extension = os.path.splitext(file_name)[

1]
    new_file_name = f"{filename_pattern}{i+1}{extension}"
    os.rename(os.path.join(directory, file_name), os.path.join(directory, new_file_name))

print("Files renamed successfully!")
```

**Exercise 10: File Merge**

Create a program that merges the contents of multiple text files into a single file. The program should ask the user for a list of file names to be merged and generate a new file containing the combined content of all the selected files.

Sample code:

```python
output_file = "merged.txt"
file_list = input("Enter a list of file names to merge (separated by commas): ").split(",")

with open(output_file, "w") as output:
    for file_name in file_list:
        with open(file_name.strip(), "r") as file:
            output.write(file.read())

print("Files merged successfully!")
```

These exercises cover various aspects of basic file management operations in Python and provide an opportunity for students to practice working with files, strings, input/output operations, and more. Feel free to modify and adapt the sample code according to your needs. Happy coding!
