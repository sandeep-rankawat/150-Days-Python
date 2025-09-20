# Chapter-1 : Introduction 
import pyjokes
print("Hello Rajveer")
print(pyjokes.get_joke())
# Comments
# This is an example of single line comment in python
"""
This is and 
example of
 multi line comment
 in python
"""
print("bye")

# Chapter-2 : Variables and Data Types
a= 4 # a is integer
b= 6.5 # b is float
c= True # c is boolean value
name = "Rajveer" # name is string
print((a+b-c)/2*5, name)

d = None

#Chapter -3 : Operators
# Airthmatic Operators (+,-,*,/, etc)
print("----- Airthmatic Operator -----")
print(a+b)
print(a-b)
print(a*b)
print(b/a)
print(a**b)
print(b//a)

#Assignment Operators (=, +=, -=, *=, **=, etc)
print("----- Assignment Operator -----")
a+=b
print(a)
b+=a
print(b)
a*=b
print(a)
a**=b
print(a)
a/=b
print(a)
a//=b
print(a)

# Comparision Operator (==, ===, >=, <=, <, >, !=, !==, etc)
print("----- Comparision Operator -----")
print(b==a)
print(b<a)
print(b<=a)
print(b>a)
print(b>=a)
print(b!=a)

# Logical Operator (and, or, not)
print("----- Logical Operator -----")
print(b!=a and b<=a)
print(b!=a and b>=a)
print(b!=a or b>=a)
print(not(b!=a) or b>=a)
