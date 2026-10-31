# Congratulations on completing Stage 1!
# I hope that test didnt give you too much trouble.


# -- Lesson 0 -- Introduction to Stage 2

# In this stage, we will cover:
# - Functions (including nested functions and closures)
# - Default parameters
# - Tuples
# - Sets
# - String methods
# - List methods
# - Dictionary methods
# - File handling
# - Exception handling
# - Classes and objects
# - Inheritance
# - Modules and packages
# - Virtual environments
# - Working with external libraries
# - More advanced data structures (like linked lists, stacks, and queues)

# Let's get started!

# -- Lesson 1 -- Functions (including nested functions and closures)

# As you may know, functions are blocks of reusable code that perform a specific task.
# They help in organizing code, improving readability, and reducing redundancy.
# Nesting is when you have blocks of code inside other blocks of code.
# A closure is a function that remembers the environment in which it was created.

# Here's a simple function that adds two numbers:
def add(a, b):
    return a + b

# You can call this function like this:
result = add(3, 5)
print("The sum of 3 and 5 is:", result)

# Now, let's look at a nested function:
def outer_function(x):
    def inner_function(y):
        return y * 2
    return inner_function(x) + 3

nested_result = outer_function(5)
print("The result of the nested function is:", nested_result)

# And here's an example of a closure:
def make_multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print("Double of 5 is:", double(5))
print("Triple of 5 is:", triple(5))

# Why care about nesting?
# Nesting helps in organizing code and creating more readable and maintainable functions.
# It allows you to encapsulate functionality and avoid polluting the global namespace.
# Closures are useful for creating functions with specific behaviors based on the environment they were created in.
# They can be used for data hiding and creating function factories.


# -- Lesson 2 -- Default Parameters

# Default parameters allow you to define default values for function parameters.
# If the caller does not provide a value for that parameter, the default value is used.

def greet(name, greeting): # No default parameter
    return f"{greeting}, {name}!"

def greet_with_default(name, greeting="Hello"): # Default parameter
    return f"{greeting}, {name}!"

print(greet("Alice", "Hi")) # Output: Hi, Alice!
print(greet_with_default("Bob")) # Output: Hello, Bob!

# Why care about default parameters?
# They make functions more flexible and easier to use.
# They allow you to provide sensible defaults while still allowing customization.
# They can help reduce the number of similar functions you need to write.
# They improve code readability by making it clear what the default behavior is.

# -- Lesson 3 -- Tuples

# Tuples are immutable sequences in Python, meaning their elements cannot be changed after creation.
# They are defined using parentheses () and can contain elements of different types.
# Tuples are often used to group related data together.
# Example of a tuple:
person = ("Alice", 30, "Engineer")
print("Person tuple:", person)
print("Name:", person[0])
print("Age:", person[1])
print("Occupation:", person[2])

# Why care about tuples?
# They are more memory efficient than lists, making them suitable for large datasets.
# They provide a way to group related data together without the overhead of a class.
# They can be used as keys in dictionaries due to their immutability.
# They help in ensuring data integrity by preventing accidental modifications.

# -- Lesson 4 -- Sets

# Sets are unordered collections of unique elements in Python.
# They are defined using curly braces {} or the set() function.
# Sets are useful for membership testing, removing duplicates, and performing mathematical set operations.

# Example of a set:
fruits = {"apple", "banana", "orange"}
print("Fruits set:", fruits)
fruits.add("grape")
print("After adding grape:", fruits)
fruits.remove("banana")
print("After removing banana:", fruits)

# Why care about sets?
# They provide efficient membership testing (checking if an element is in the set).
# They automatically handle duplicates, ensuring all elements are unique.
# They support mathematical set operations like union, intersection, and difference.
# They can be used to simplify code when dealing with collections of unique items.

# -- Lesson 5 -- String Methods

# Strings in Python come with a variety of built-in methods that allow you to manipulate and analyze text data.
# Here are some commonly used string methods:
text = "  Hello, World!  "
print("Original text:", text)
print("Stripped text:", text.strip())
print("Uppercase text:", text.upper())
print("Lowercase text:", text.lower())
print("Replaced text:", text.replace("World", "Python"))

# In stage 1, we covered what these methods are, but not really when or why to use them.
# Lets go over that now.

# When to use string methods:
# Use string methods when you need to manipulate or analyze text data.
# They are useful for cleaning up user input, formatting output, and extracting information from strings.

# Why use string methods:
# They provide a convenient way to perform common text operations without writing custom code.
# They improve code readability by making it clear what operation is being performed.
# They can help prevent errors by handling edge cases (e.g., stripping whitespace).

# -- Lesson 6 -- List Methods

# Lists in Python come with a variety of built-in methods that allow you to manipulate and analyze list data.
# Here are some commonly used list methods:
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

# In stage 1, we only used append, and did not cover when or why to use these methods.
# Lets go over that now.

# When to use list methods:
# Use list methods when you need to manipulate or analyze list data.
# They are useful for adding, removing, sorting, and searching for elements in a list.

# Why use list methods:
# They provide a convenient way to perform common list operations without writing custom code.
# They improve code readability by making it clear what operation is being performed.
# They can help catch errors early (e.g., removing an element that doesn't exist raises a ValueError).

# -- Lesson 7 -- Dictionary Methods

# Dictionaries in Python are collections of key-value pairs.
# They are defined using curly braces {} with key-value pairs separated by colons.
# Dictionaries are useful for storing and retrieving data based on unique keys.

# Example of a dictionary:
person = {"name": "Alice", "age": 30, "occupation": "Engineer"}
print("Person dictionary:", person)
print("Name:", person["name"])
print("Age:", person["age"])
print("Occupation:", person["occupation"])

# Why care about dictionaries?
# They provide a way to store and retrieve data using meaningful keys.
# They allow for fast lookups, making them suitable for large datasets.
# They can be easily converted to and from other data formats (e.g., JSON).
# They help in organizing related data together in a structured way.

# -- Lesson 8 -- File Handling

# File handling is an important aspect of programming that allows you to read from and write to files.
# In Python, you can work with files using built-in functions and methods.

# Here are some common file handling operations:
# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a sample file.\n")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print("File content:")
    print(content)

# Appending to a file
with open("example.txt", "a") as file:
    file.write("Appending a new line.\n")

# Why care about file handling?
# It allows you to persist data between program executions.
# It enables you to work with large datasets that may not fit in memory.
# It provides a way to share data between different programs and systems.
# It is essential for tasks like logging, configuration management, and data analysis.

# -- Lesson 9 -- Exception Handling

# Exception handling is a mechanism in Python that allows you to handle errors gracefully.
# It helps in preventing program crashes and provides a way to recover from errors.
# You can use try, except, else, and finally blocks to handle exceptions.
# Example of exception handling:
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print("Result:", result)
finally:
    print("Execution completed.")

# Why care about exception handling?
# It improves the robustness and reliability of your code.
# It allows you to handle unexpected situations without crashing the program.
# It provides a way to log errors and debug issues.
# It enhances user experience by providing meaningful error messages.

# -- Lesson 10 -- Classes and Objects

# As we went over in stage 1, classes are blueprints for creating objects.
# They encapsulate data and behavior related to that data.
# Objects are instances of classes that hold specific data and can perform actions defined by the class.
# Example of a class and object:
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

# Why care about classes and objects?
# They help in organizing code and promoting code reuse.
# They provide a way to model real-world entities and their behaviors.
# They support encapsulation, allowing you to hide implementation details.
# They enable inheritance and polymorphism, promoting code flexibility and extensibility.

# -- Lesson 11 -- Inheritance

# Inheritance is a mechanism in object-oriented programming that allows a class
# to inherit properties and methods from another class.
# The class that inherits is called the child class or subclass
# and the class being inherited from is called the parent class or superclass.
# Example of inheritance:

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

# The dog class inherits from the animal class, meaning it has access to its properties and methods.
# Why care about inheritance?
# It promotes code reuse by allowing you to build upon existing classes.
# It helps in organizing code and creating a hierarchical structure.
# It enables polymorphism, allowing you to use objects of different classes interchangeably.
# It simplifies code maintenance by centralizing common functionality in a base class.

# -- Lesson 12 -- Modules and Packages

# Modules are files containing Python code that can define functions, classes, and variables.
# They help in organizing code into manageable and reusable components.
# Packages are collections of modules organized in directories.
# They provide a way to structure larger projects and avoid naming conflicts.
# Example using the my_module.py file:

import my_module

my_instance = my_module.MyModule("Alice")
print(my_instance.greet())

# Why care about modules and packages?
# They help in organizing code into logical units, making it easier to manage and maintain.
# They promote code reuse by allowing you to import and use code from other files.
# They help in avoiding naming conflicts by providing namespaces.
# They enable collaboration by allowing multiple developers to work on different modules or packages.

'''
DISCLAIMER:
# The following lessons (13 and 14) are more advanced topics that may not be necessary for all Python users.
# It is recommended to explore these topics only if you are interested in deepening your understanding of Python
# They also will not have any code examples, as they are more conceptual in nature.
'''


# -- Lesson 13 -- Virtual Environments

# Yikes, things are getting complicated now.

# A virtual environment is an isolated Python environment that allows you to manage dependencies for different projects separately.
# It helps in avoiding conflicts between packages and ensures that each project has its own set of dependencies
# without affecting the global Python installation.
# You can create a virtual environment using the venv module:
# python -m venv myenv

# To activate the virtual environment:
# On Windows:
# myenv\Scripts\activate
# On macOS and Linux:
# source myenv/bin/activate
# To deactivate the virtual environment:
# deactivate

# Why care about virtual environments?
# They help in managing project-specific dependencies, ensuring that each project has the required packages and versions
# They prevent conflicts between packages used in different projects
# They allow you to experiment with different package versions without affecting the global Python installation
# They promote best practices in Python development by encouraging isolation and reproducibility

# -- Lesson 14 -- Working with External Libraries

# External libraries are packages or modules that are not included in the standard Python library.
# They provide additional functionality and tools that can help you accomplish specific tasks more efficiently.
# You can install external libraries using package managers like pip.
# For example, there is a very popular library named Pygame that is used for game development.
# To install Pygame, you can use the following command:
# pip install pygame
# Once installed, you can import and use the library in your Python code:

# We won't go over Pygame here, but you can check out the documentation at https://www.pygame.org/docs/

# Why care about external libraries?
# They provide additional functionality and tools that can help you accomplish specific tasks more efficiently.
# They save development time by providing pre-built solutions for common problems.
# They allow you to leverage the expertise of the Python community and access a wide range of resources
# They promote code reuse and collaboration by allowing you to share and use code from other developers

# -- Lesson 15 -- More Advanced Data Structures (like linked lists, stacks, and queues)

# In addition to the built-in data structures like lists, tuples, sets, and dictionaries,
# Python also supports more advanced data structures like linked lists, stacks, and queues.
# These data structures provide different ways to organize and manipulate data based on specific requirements.
# Linked Lists are linear data structures where each element (node) points to the next node in the sequence.
# Stacks are Last In First Out (LIFO) data structures where the last element added is the first one to be removed.
# Queues are First In First Out (FIFO) data structures where the first element added is the first one to be removed.

# Example of a simple stack using a list:
stack = []
stack.append(1)
stack.append(2)
stack.pop()

print("Stack after pushing 1 and 2, then popping:", stack)

# Example of a simple queue using collections.deque:
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.popleft()

print("Queue after enqueuing 1 and 2, then dequeuing:", queue)

# Why care about advanced data structures?
# They provide different ways to organize and manipulate data based on specific requirements.
# They can improve the efficiency of certain operations (e.g., adding/removing elements).
# They help in solving specific problems that require specialized data handling (e.g., implementing algorithms).
# They enhance your understanding of data organization and algorithm design, which are fundamental concepts in computer science.

# -- CONGRATULATIONS!! --

# You have finished Stage 2 of the Python Tutorial!
# You should now have a solid understanding of more advanced Python concepts and be ready to tackle more complex projects.

def end():
    print("Congratulations on completing Stage 2!")

end()