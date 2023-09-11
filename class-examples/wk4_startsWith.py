# Example 1: Basic usage
text = "Hello, world!"
if text.startswith("Hello"):
    print("The string starts with 'Hello'")
else:
    print("The string does not start with 'Hello'")

# Example 2: Case-insensitive check
text = "Python is awesome"
prefix = "python"
if text.lower().startswith(prefix.lower()):
    print("The string starts with 'python' (case-insensitive)")

# Example 3: Check with multiple prefixes
text = "Apples are delicious"
prefixes = ["Apples", "Bananas", "Oranges"]
for prefix in prefixes:
    if text.startswith(prefix):
        print(f"The string starts with '{prefix}'")

# Example 4: Check with a tuple of prefixes
text = "The quick brown fox"
prefix_tuple = ("The", "A", "An")
if text.startswith(prefix_tuple):
    print("The string starts with one of the prefixes in the tuple")

# Example 5: Using start and end parameters
text = "Python programming is fun"
prefix = "Python"
if text.startswith(prefix, 0, 6):  # Check only the first 6 characters
    print("The string starts with 'Python' in the first 6 characters")
