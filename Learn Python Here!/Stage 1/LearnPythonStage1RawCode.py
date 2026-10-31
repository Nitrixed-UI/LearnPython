import os

text = "Hello"
number = 10
pi = 3.14
is_cool = True

Box1 = "Hello, World!"
Box2 = True
Box3 = 32897

print(Box1)
print(Box2)
print(Box3)

for num in [1, 2, 3, 4, 5]:
    print(num)

for i in range(5):
    print(i)

a = 5

while a < 10:
    print(a)
    a = a + 1

while True:
    print("This runs forever unless you break it!")
    break

def myFunction():
    print("Function")
    print("Lol")

myFunction()

def mySecondFunction(argument1: int):
    print(argument1 + argument1)


mySecondFunction(5)

def add(a, b):
    return a + b


result = add(3, 4)
print(result)

class Test:
    def __init__(self, age: int, name: str):
        self.age = age
        self.name = name

    def introduce(self):
        print(f"{self.name} says hello!")


Test1 = Test(15, "Bryson")
Test2 = Test(20, "Ava")

Test1.introduce()
Test2.introduce()

import time

print(time.time())

import random

print(random.randint(1, 10))

from functools import wraps

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

@tickTock
def my_function():
    time.sleep(1)
    return "Done"

my_function()

if 10 > 0:
    print("10 is greater than 0!")

if 5 > 100:
    print("5 is greater than 100!")
else:
    print("5 is not greater than 100!")

if 5 > 100:
    print("5 is greater than 100!")
elif 5 > 50:
    print("5 is greater than 50!")
elif 5 > 10:
    print("5 is greater than 10!")
else:
    print("All previous statements failed!")

x = 42

if x > 100:
    print("x is really big!")
elif x > 50:
    print("x is kinda big!")
elif x > 10:
    print("x is moderate.")
else:
    print("x is small.")

list1: list = []

list1 = ["Hello!", True, 100]

list1.append("Hello!")
list1.append(True)
list1.append(100)

for item in range(len(list1)):
    print(list1[item])
    
dictionary1: dict = {}

dictionary1["name"] = "Bryson"
dictionary1["age"] = 15

print(dictionary1["name"])
print(dictionary1["age"])

dictionary2: dict = {
    "name": "Ava",
    "age": 14
}

for key in dictionary2:
    print(f"{key}: {dictionary2[key]}")

def apply_function(func, value):
    return func(value)

def square(x):
    return x * x

def cube(x):
    return x * x * x

result1 = apply_function(square, 3)
result2 = apply_function(cube, 3)

print(result1)
print(result2)

def outer_function():
    def inner_function():
        return "Hello from the inner function!"
    return inner_function

new_function = outer_function()
print(new_function())

def make_multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))
print(triple(5))

def greet(name, message="Hello"):
    return f"{message}, {name}!"

print(greet("Alice"))
print(greet("Bob", "Goodbye"))

tuple1: tuple = (1, 2, 3, "Hello", True)

for item in tuple1:
    print(item)

set1: set = {1, 2, 3, "Hello", True}

set1.add(4)
set1.add("World")

set1.remove(2)

for item in set1:
    print(item)

text: str = "I used Mixed CASE and trailing white space!   "

print(text.lower())
print(text.upper())
print(text.title())
print(text.strip())

print(text.replace("Mixed CASE", "mixed case"))
print(text.split())

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print("Result:", result)
finally:
    print("Execution completed.")

user_input = input("Enter something: ")
print("You entered:", user_input)

age = int(input("Enter your age: "))
print("You are", age, "years old.")
