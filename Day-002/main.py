# Chapter-4 :
# Section A:  Type() and Type Conversion
a = "31.5"
b = float(a) # converting string to float
print(type(a))
print(type(b))

# Section B: Input from user
name = input("Enter your name: ")
print(name)

a  = int(input("Enter a number1 "))
b  = int(input("Enter a number2 "))
print(a+b)

# Chapter-5: String and its method
a = 'Hello World'
b = "Good Morning ! Sir,"
c = '''How Can I help You, Sir?'''

# Section A- String Slicing
myName = "Sandeep_Rankawat"
myNameShort = myName[0:7]
myNameShort = myName[-7:-1]
myNameShort = myName[:9]
myNameShort = myName[1:]
myNameShort = myName[::5]
print(myNameShort)

# Section B- Funtions and methods
myName = "sandeep_Rankawat"
print(len(myName))
print(myName.endswith("at"))
print(myName.endswith("ar"))
print(myName.startswith("san"))
print(myName.startswith("San"))
print(myName.capitalize())
print(myName.upper())
print(myName.lower())
print(myName.find("a"))
print(myName.replace("a", "e"))

# Section C- Escape Sequence Character
#   \n, \t, \;, \\ etc 

string = "This is first line string. \nThis is second line  string"
string = "This is first line string. \n\tThis is \"second\" line  string"
print(string)

