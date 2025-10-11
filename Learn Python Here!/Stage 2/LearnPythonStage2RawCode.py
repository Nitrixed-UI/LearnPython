def add(a, b):
    return a + b

result = add(3, 5)
print("The sum of 3 and 5 is:", result)

def outer_function(x):
    def inner_function(y):
        return y * 2
    return inner_function(x) + 3

nested_result = outer_function(5)
print("The result of the nested function is:", nested_result)

def make_multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print("Double of 5 is:", double(5))
print("Triple of 5 is:", triple(5))

def greet(name, greeting):
    return f"{greeting}, {name}!"

def greet_with_default(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice", "Hi"))
print(greet_with_default("Bob"))

person = ("Alice", 30, "Engineer")
print("Person tuple:", person)
print("Name:", person[0])
print("Age:", person[1])
print("Occupation:", person[2])

fruits = {"apple", "banana", "orange"}
print("Fruits set:", fruits)
fruits.add("grape")
print("After adding grape:", fruits)
fruits.remove("banana")
print("After removing banana:", fruits)

text = "  Hello, World!  "
print("Original text:", text)
print("Stripped text:", text.strip())
print("Uppercase text:", text.upper())
print("Lowercase text:", text.lower())
print("Replaced text:", text.replace("World", "Python"))

numbers = [1, 2, 3, 4, 5]
print("Original list:", numbers)
numbers.append(6)
print("After appending 6:", numbers)
numbers.remove(3)
print("After removing 3:", numbers)
numbers.sort(reverse=True)
print("After sorting in descending order:", numbers)
print("Index of 4:", numbers.index(4))
print("Count of 2:", numbers.count(2))
numbers.clear()
print("After clearing the list:", numbers)

person = {"name": "Alice", "age": 30, "occupation": "Engineer"}
print("Person dictionary:", person)
print("Name:", person["name"])
print("Age:", person["age"])
print("Occupation:", person["occupation"])

with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a sample file.\n")

with open("example.txt", "r") as file:
    content = file.read()
    print("File content:")
    print(content)

with open("example.txt", "a") as file:
    file.write("Appending a new line.\n")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print("Result:", result)
finally:
    print("Execution completed.")

class Pig:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def oink(self):
        return f"{self.name} says Oink!"
    
my_pig = Pig("Porky", "Yorkshire")

print("Pig's name:", my_pig.name)
print("Pig's breed:", my_pig.breed)
print(my_pig.oink())

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return f"{self.name} barks."
    
my_dog = Dog("Buddy", "Golden Retriever")

print("Dog's name:", my_dog.name)
print("Dog's breed:", my_dog.breed)
print("Dog's sound:", my_dog.speak())

import my_module

my_instance = my_module.MyModule("Alice")
print(my_instance.greet())

stack = []
stack.append(1)
stack.append(2)
stack.pop()

print("Stack after pushing 1 and 2, then popping:", stack)

from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.popleft()

print("Queue after enqueuing 1 and 2, then dequeuing:", queue)

def end():
    print("Congratulations on completing Stage 2!")

end()