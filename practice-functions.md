Here are ten practice problems related to functions in Python along with their answer code. These exercises cover the use of the `def` keyword, working with different numbers of arguments, and returning values from functions:

**1. Define a function that takes no arguments and prints "Hello, World!" when called.**

```python
def hello_world():
    print("Hello, World!")

# Call the function
hello_world()
```

**2. Create a function that takes two numbers as arguments and returns their sum.**

```python
def add_numbers(num1, num2):
    return num1 + num2

# Call the function
result = add_numbers(5, 3)
print(result)  # Should print 8
```

**3. Write a function that accepts a list of numbers and returns their average.**

```python
def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

# Call the function
numbers_list = [4, 6, 8, 10]
avg = calculate_average(numbers_list)
print(avg)  # Should print 7.0
```

**4. Define a function that takes a string as an argument and returns its length.**

```python
def string_length(text):
    return len(text)

# Call the function
length = string_length("Python is fun")
print(length)  # Should print 13
```

**5. Create a function that calculates the factorial of a given number.**

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Call the function
result = factorial(5)
print(result)  # Should print 120
```

**6. Write a function that checks if a given number is even.**

```python
def is_even(num):
    return num % 2 == 0

# Call the function
print(is_even(4))  # Should print True
print(is_even(7))  # Should print False
```

**7. Define a function that takes a list of strings and returns a new list with the strings in uppercase.**

```python
def uppercase_strings(strings):
    return [s.upper() for s in strings]

# Call the function
words = ["apple", "banana", "cherry"]
result = uppercase_strings(words)
print(result)  # Should print ['APPLE', 'BANANA', 'CHERRY']
```

**8. Create a function that checks if a given string is a palindrome (reads the same forwards and backwards).**

```python
def is_palindrome(s):
    s = s.lower()  # Convert to lowercase for case-insensitive comparison
    return s == s[::-1]

# Call the function
print(is_palindrome("racecar"))  # Should print True
print(is_palindrome("hello"))    # Should print False
```

**9. Write a function that takes a dictionary and returns a list of its keys.**

```python
def get_keys(dictionary):
    return list(dictionary.keys())

# Call the function
my_dict = {"name": "Alice", "age": 30, "city": "Orlando"}
keys = get_keys(my_dict)
print(keys)  # Should print ['name', 'age', 'city']
```

**10. Define a function that calculates the square of all numbers in a given list and returns a new list with the squared values.**

```python
def square_numbers(numbers):
    return [x ** 2 for x in numbers]

# Call the function
nums = [1, 2, 3, 4, 5]
squared = square_numbers(nums)
print(squared)  # Should print [1, 4, 9, 16, 25]
```

These practice problems cover a range of concepts related to Python functions and provide practice on how to define and use functions effectively.
