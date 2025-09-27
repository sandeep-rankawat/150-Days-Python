# Python Day 2 - Type Conversion and Strings

This repository contains Python code examples covering type conversion, user input, and string manipulation concepts from Day 2 of Python learning.

## Chapter 4: Type Conversion and User Input

### Section A: Type() and Type Conversion
Learn how to check data types and convert between different data types in Python.

```python
a = "31.5"
b = float(a) # converting string to float
print(type(a))
print(type(b))
```

### Section B: Input from User
Examples of taking user input and converting it to appropriate data types.

```python
name = input("Enter your name: ")
print(name)
a = int(input("Enter a number1 "))
b = int(input("Enter a number2 "))
print(a+b)
```

## Chapter 5: Strings and String Methods

### String Declaration
Different ways to declare strings in Python using single quotes, double quotes, and triple quotes.

```python
a = 'Hello World'
b = "Good Morning ! Sir,"
c = '''How Can I help You, Sir?'''
```

### Section A: String Slicing
Learn how to extract parts of strings using various slicing techniques.

```python
myName = "Sandeep_Rankawat"
myNameShort = myName[0:7]    # First 7 characters
myNameShort = myName[-7:-1]  # Last 6 characters (excluding last)
myNameShort = myName[:9]     # First 9 characters
myNameShort = myName[1:]     # All characters except first
myNameShort = myName[::5]    # Every 5th character
print(myNameShort)
```

### Section B: String Functions and Methods
Common string methods for manipulation and information retrieval.

```python
myName = "sandeep_Rankawat"
print(len(myName))              # Length of string
print(myName.endswith("at"))    # Check if ends with "at"
print(myName.endswith("ar"))    # Check if ends with "ar"
print(myName.startswith("san")) # Check if starts with "san"
print(myName.startswith("San")) # Case sensitive check
print(myName.capitalize())      # Capitalize first letter
print(myName.upper())           # Convert to uppercase
print(myName.lower())           # Convert to lowercase
print(myName.find("a"))         # Find index of character "a"
print(myName.replace("a", "e")) # Replace "a" with "e"
```

### Section C: Escape Sequence Characters
Special characters used in strings for formatting and special purposes.

```python
# Common escape sequences: \n (newline), \t (tab), \" (quote), \\ (backslash)

string = "This is first line string. \nThis is second line  string"
string = "This is first line string. \n\tThis is \"second\" line  string"
print(string)
```

## Key Concepts Covered

- **Type Checking**: Using `type()` function to check data types
- **Type Conversion**: Converting between strings, integers, and floats
- **User Input**: Taking input from users and converting to appropriate types
- **String Slicing**: Extracting substrings using index notation
- **String Methods**: Built-in functions for string manipulation
- **Escape Sequences**: Special characters for formatting strings

## Running the Code

To run any of these examples, save them in a `.py` file and execute using:

```bash
python filename.py
```

Make sure you have Python installed on your system before running the code examples.