# LEARN PYTHON

import os

# -- Lesson 0 -- Introduction to Python

# There are many types of data, often called DataTypes.
# DataTypes hold data according to their types.


# -- Lesson 1 -- Variables

# A variable is a name that holds data.
# Think of variables like a box, you give the box a name, you put in data, and you can neatly
# hand out the box to people who need it.

# Variables can hold different types of data:
text = "Hello"  # string
number = 10  # integer
pi = 3.14  # float
is_cool = True  # boolean


# E.X

Box1 = "Hello, World!"
Box2 = True
Box3 = 32897

# Now, use the print function to show it to the console!

print(Box1)
print(Box2)
print(Box3)


# Output:
# Hello, World!
# True
# 32897


# -- Lesson 2 -- For loops

# a for loop can be thought of like this:
# For (the amount of something), do (this).

# E.X

for num in [1, 2, 3, 4, 5]:
    print(num)

# Output:
# 1 
# 2 
# 3 
# 4 
# 5


# The most common way to use for loops is by using the range() function.

for i in range(5):
    print(i)

# Output:
# 0 
# 1 
# 2 
# 3 
# 4

# IMPORTANT NOTE: With one number, it starts at 0 and stops BEFORE that number.
# You can pick the start too: range(2, 5) gives 2, 3, 4.


# -- Lesson 3 -- While loops

# a while loop can be thought of like this:
# While (condition) is true, do (this)

# E.X

a = 5

while a < 10:
    print(a)
    a = a + 1

# Output :
# 5
# 6
# 7
# 8
# 9
# This wont print out 10 because when 
# it hits 10, it exits the loop.

# Be careful: without the break below, this loop would never end!
while True:
    print("This runs forever unless you break it!")
    break  # Stops the loop

# Avoid from using infinite loops, it can cause your program
# to crash, freeze, or use up all your CPU.


# -- Lesson 4 -- Functions

# Oh boy, here comes the hard part to understand.
# A function can be thought of as a 
# variable that hold many lines of code.

# E.X

# Def - Define the function
def myFunction():
    print("Function")
    print("Lol")


# Need to call the function after it has been defined.
myFunction()

# Output: 
# Function 
# Lol

# You use these when you want to avoid typing out tons of code.
# You can pass in arguments into your function and use them.

# E.X


def mySecondFunction(argument1: int):
    print(argument1 + argument1)


mySecondFunction(5)

# Output: 
# 10

# This is just scratching the surface of 
# what you can do with functions.

# Now, you're going to need to know when to return values.
# Returning values sends a value back out of the function.


def add(a, b):
    return a + b


result = add(3, 4)
print(result)
# Output:
# 7


# -- Lesson 5 -- Classes

# Now here is where it gets REALLY hard to follow along with
# Good Luck!

# Classes are like blueprints; They give instructions 
# on how to build something.
# (Yes this is technically OOP)

# Define a class using the keyword "class"
# You usually want to make a function inside of the class named "__init__".
# This function stands for "Initiate" or "Initialize".
# This runs every time a new Object is made.


class Test:
    def __init__(self, age: int, name: str):  # Give the Test class an age and a name.
        self.age = age
        self.name = name

    def introduce(self):  # Now you can make your own functions
        print(f"{self.name} says hello!")  # This one uses the name stored in the object.


Test1 = Test(15, "Bryson")
Test2 = Test(20, "Ava")

Test1.introduce()  # Bryson says hello!
Test2.introduce()  # Ava says hello!


# IMPORTANT: self means the object that is using the function.
# It is not a keyword, just the name everyone uses for that first parameter.

# Please please PLEASE refer to 
# https://docs.python.org/3/reference/datamodel.html#object.__init__
# for more info in classes.
# (Yes its a shit ton of reading im sorry)

# -- Lesson 6 -- Importing Libraries

# To import a lib (library), 
# you need to use the keyword, import

import time

# This lets your code use the functions in the time library.
# It is part of the standard library, which comes with Python.
# Some examples of the time functions is:
print(time.time())  # Prints the current time in Seconds.

# Another Example of a library's functions:

import random

print(random.randint(1, 10))  # Prints a random number between 1 and 10


# Heres a useful function you might 
# make using the time.perf_counter() function.

from functools import wraps  # Imports a specific tool from a new lib


def tickTock(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        duration = end_time - start_time
        print(f"{func.__name__} executed in {duration:.6f} seconds")
        return result

    return wrapper


# Uses a decorator to define the new function. 
# This means it will run the function through another.
@tickTock
def my_function():
    time.sleep(1)
    return "Done"


my_function()

# Output (the exact time will vary a little):
# my_function executed in 1.000512 seconds


# -- Lesson 7 -- If Statements

# An if statement checks if the condition after it
# is true, and if it is, runs the following code.

# E.X

if 10 > 0:
    print("10 is greater than 0!")

# if Statements are often paired with the else and elif keywords.
# else - if the previous statement is false, do this.

if 5 > 100:
    print("5 is greater than 100!")
else:
    print("5 is not greater than 100!")

# elif - if the previous conditions were false, and this one is true, do this.

if 5 > 100:
    print("5 is greater than 100!")
elif 5 > 50:
    print("5 is greater than 50!")
elif 5 > 10:
    print("5 is greater than 10!")
else:
    print("All previous statements failed!")

# Remember: indentation (the spaces before each line) matters in Python!
# The code inside the if, elif, or else block must be indented properly.
# Example using the previously learnt Variables:

x = 42

if x > 100:
    print("x is really big!")
elif x > 50:
    print("x is kinda big!")
elif x > 10:
    print("x is moderate.")
else:
    print("x is small.")


# -- Lesson 8 -- Lists and Dictionaries

# In Python, a List is defined by the name of the list, then brackets.
# Example:

list1: list = []

# ANYTHING can go into a list.
# You can put strings, integers, booleans, floats, and even other lists and dictionaries!
# You can either define a list like above, or you can define it with data in it.

list1 = ["Hello!", True, 100]

# You can also add data to a list after it has been defined.
# Use list_name.append(item_to_append) to add something to a list.

list1.append("Hello!")
list1.append(True)
list1.append(100)

# You can use a for loop to easily print the contents in a list!
# Use len(LIST) to get the number of items in the list!

for item in range(len(list1)):
    print(list1[item])
    
# A dictionary is a glorified list for lack
# of a better term.
# They can be defined by using dict_name = {}

dictionary1: dict = {}

# You can add items to a dictionary by using
# dict_name[key] = value

dictionary1["name"] = "Bryson"
dictionary1["age"] = 15

# You can access items in a dictionary by using
# dict_name[key]

print(dictionary1["name"])  # Bryson
print(dictionary1["age"])  # 15

# It's pretty customary to
# give the dict data before you use it.
# This is how you would format it.

dictionary2: dict = {
    "name": "Ava",
    "age": 14
}

for key in dictionary2:
    print(f"{key}: {dictionary2[key]}")

# Output:
# name: Ava
# age: 14

# -- Lesson 9 -- Advanced Functions

# Functions can take in other functions as arguments.
# Although rare, it can be useful in some situations.

def apply_function(func, value):
    return func(value)

# Why is this useful?
# Imagine you have a function that does something,
# but you want to be able to change what it does without
# rewriting the whole function.

def square(x):
    return x * x

def cube(x):
    return x * x * x

result1 = apply_function(square, 3)  # 9
result2 = apply_function(cube, 3)    # 27

print(result1)
print(result2)

# Output:
# 9
# 27

# Functions can also return other functions.

def outer_function():
    def inner_function():
        return "Hello from the inner function!"
    return inner_function

new_function = outer_function()
print(new_function())

# Output:
# Hello from the inner function!

# Why is this useful?
# It allows you to create function factories,
# where you can generate functions with specific behaviors.

def make_multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15

# Output:
# 10
# 15

# Lastly, functions can have default arguments.
def greet(name, message="Hello"):
    return f"{message}, {name}!"

print(greet("Alice"))  # Hello, Alice!
print(greet("Bob", "Goodbye"))  # Goodbye, Bob!

# Output:
# Hello, Alice!
# Goodbye, Bob!

# Default arguments are useful when you want to provide a common value
# but still allow for customization when needed.

# -- Lesson 10 -- Tuples and Sets

# A tuple is similar to a list, but it is immutable (cannot be changed after creation).
# Tuples are defined using parentheses ().

tuple1: tuple = (1, 2, 3, "Hello", True)

# Similarly to a list, using for loops to access items in a tuple is common.
for item in tuple1:
    print(item)

# Output:
# 1
# 2
# 3
# Hello
# True

# A set is a collection of unique items.
# Sets are defined using curly braces {}.
# (But an empty {} is a dictionary. Use set() for an empty set.)

set1: set = {1, 2, 3, "Hello", True}

# You can add items to a set using the add() method.
set1.add(4)
set1.add("World")

# You can also remove items using the remove() method.
set1.remove(2)

# Using a for loop to access items in a set is also common.
for item in set1:
    print(item)

# Output (sets have no fixed order, so yours may be in a different order):
# 1
# 3
# 4
# Hello
# World
# True is missing because Python treats True and 1 as equal,
# so the set only keeps one of them.

# Why are these useful?
# Tuples are useful when you want to ensure that the data cannot be modified.
# Sets are useful when you want to store unique items and need fast membership testing.
# For example, checking if an item is in a set is much faster than checking in a list.


# -- Lesson 11 -- String Operations

# Strings are sequences of characters.
# You can use various operations to manipulate strings.

text: str = "I used Mixed CASE and trailing white space!   "

# Common string operations include:
print(text.lower())  # Converts to lowercase
print(text.upper())  # Converts to uppercase
print(text.title())  # Converts to title case
print(text.strip())  # Removes leading and trailing whitespace

# Why use these?
# These operations are useful for normalizing and cleaning up text data,
# making it easier to work with and analyze.

print(text.replace("Mixed CASE", "mixed case"))  # Replaces a substring
print(text.split())  # Splits the string into a list of words

# -- Lesson 12 -- Exception Handling

# In Python, exceptions are errors that occur during the execution of a program.
# You can handle these exceptions using try and except blocks.

try:
    # Code that may raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Code to handle the exception
    print("Error: Division by zero is not allowed.")
else:
    # Code to run if no exception occurs
    print("Result:", result)

finally:
    # Code that always runs, regardless of exceptions
    print("Execution completed.")

# To put it simply:
# It will try and do something,
# if it fails, it will do something else,
# if it succeeds, it will do something else,
# and it will always do something at the end.

# Why is this useful?
# Exception handling is crucial for building robust 
# programs that can gracefully handle errors
# without crashing, providing a better user experience.

# -- Lesson 13 -- User Input

# You can get input from the user using the input() function.
# This function reads a line from input, 
# converts it to a string (stripping a trailing newline), and returns that.

user_input = input("Enter something: ")
print("You entered:", user_input)

# You can also convert the input to other data types,
# such as integers or floats, if needed.

age = int(input("Enter your age: "))
print("You are", age, "years old.")

# Why is this useful?
# User input is essential for interactive programs,
# allowing users to provide data and make choices.

# -- CONGRATULATIONS!! --

# You have finished Stage 1 of the Python Tutorial!
# You should now know the basics of Python programming.
# Please take the TEST #1.py and see just how much you retained!

# If you want to learn more, please refer to the official Python documentation:
# https://docs.python.org/3/tutorial/index.html

# Happy Coding!!!