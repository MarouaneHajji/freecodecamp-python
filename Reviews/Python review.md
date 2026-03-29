# 🐍 Python Review — Complete Reference

> A comprehensive reference covering Python fundamentals through advanced topics including OOP, data structures, algorithms, and dynamic programming.

---

## Table of Contents

1. [What is Python?](#1-what-is-python)
2. [Variables](#2-variables)
3. [Comments & Print](#3-comments--print)
4. [Data Types](#4-data-types)
5. [Working with Strings](#5-working-with-strings)
6. [Numbers & Math Operations](#6-numbers--math-operations)
7. [Functions](#7-functions)
8. [Scope](#8-scope)
9. [Control Flow](#9-control-flow)
10. [Loops](#10-loops)
11. [Lists](#11-lists)
12. [Tuples](#12-tuples)
13. [Dictionaries](#13-dictionaries)
14. [Sets](#14-sets)
15. [List Comprehensions & Iterable Functions](#15-list-comprehensions--iterable-functions)
16. [Lambda Functions](#16-lambda-functions)
17. [Python Standard Library & Imports](#17-python-standard-library--imports)
18. [Error Handling & Exceptions](#18-error-handling--exceptions)
19. [Object-Oriented Programming (OOP)](#19-object-oriented-programming-oop)
20. [Algorithms & Big O Notation](#20-algorithms--big-o-notation)
21. [Data Structures](#21-data-structures)
22. [Searching Algorithms](#22-searching-algorithms)
23. [Sorting Algorithms](#23-sorting-algorithms)
24. [Graphs](#24-graphs)
25. [Trees](#25-trees)
26. [Priority Queues & Heaps](#26-priority-queues--heaps)
27. [Dynamic Programming](#27-dynamic-programming)

---

## 1. What is Python?

Python is a general-purpose programming language known for its simplicity and ease of use. It is used in:

- Data Science & Machine Learning
- Web Development
- Scripting & Automation
- Cybersecurity
- Embedded Systems & IoT (Raspberry Pi, MicroPython)

**Installation:** Download from [python.org](https://www.python.org/)

---

## 2. Variables

```python
name = 'John Doe'
age = 25
```

### Naming Conventions

- Must start with a letter or underscore (`_`), not a number
- Can only contain alphanumeric characters and underscores
- Case-sensitive (`age`, `Age`, `AGE` are all different)
- Cannot use reserved keywords (`if`, `class`, `def`, etc.)
- Multiple words use `snake_case`

---

## 3. Comments & Print

```python
# This is a single line comment

"""
This is a multi-line string.
Often used for documentation or commenting out blocks.
"""

print('Hello world!')  # Hello world!
```

---

## 4. Data Types

Python is dynamically typed — you don't need to declare types explicitly.

| Type        | Example                              | Mutable |
|-------------|--------------------------------------|---------|
| `int`       | `10`                                 | ❌       |
| `float`     | `4.50`                               | ❌       |
| `str`       | `'hello'`                            | ❌       |
| `bool`      | `True`                               | ❌       |
| `tuple`     | `(7, 5, 8)`                          | ❌       |
| `range`     | `range(5)`                           | ❌       |
| `NoneType`  | `None`                               | ❌       |
| `list`      | `[22, 'Hello', 3.14, True]`          | ✅       |
| `set`       | `{7, 5, 8}`                          | ✅       |
| `dict`      | `{"name": "Alice", "age": 25}`       | ✅       |

```python
# Check the type of a variable
print(type(42))           # <class 'int'>
print(type(3.14))         # <class 'float'>

# Check if a variable matches a type
print(isinstance('hello', str))  # True
print(isinstance('hello', int))  # False
```

### Truthy and Falsy Values

**Falsy:** `None`, `False`, `0`, `0.0`, `''`, empty collections  
**Truthy:** Non-zero numbers, non-empty strings, non-empty collections

```python
print(bool(0))       # False
print(bool(''))      # False
print(bool(1))       # True
print(bool('Hi'))    # True
```

---

## 5. Working with Strings

```python
developer = 'Jessica'
city = "Los Angeles"
```

### Accessing Characters

```python
my_str = 'Hello world'
print(my_str[0])   # H
print(my_str[-1])  # d  (negative indexing from end)
```

### Escaping & Concatenation

```python
msg = 'It\'s a sunny day'

# Concatenation
print('My name is ' + developer + '.')

# f-strings (preferred)
greeting = f'My name is {developer}.'
```

### Slicing

```python
# str[start:stop:step]
message = 'Python is fun!'
print(message[0:6])   # Python
print(message[7:])    # is fun!
print(message[::2])   # Pto sfn
```

### Common String Methods

```python
s = 'hello world'

s.upper()              # 'HELLO WORLD'
s.lower()              # 'hello world'
s.strip()              # removes leading/trailing whitespace
s.replace('hello', 'hi')  # 'hi world'
s.split(' ')           # ['hello', 'world']
' '.join(['a', 'b'])   # 'a b'
s.startswith('he')     # True
s.endswith('ld')       # True
s.find('world')        # 6  (-1 if not found)
s.count('l')           # 3
s.capitalize()         # 'Hello world'
s.title()              # 'Hello World'
s.isupper()            # False
s.islower()            # True
len(s)                 # 11
'world' in s           # True
```

---

## 6. Numbers & Math Operations

### Basic Operations

```python
# Addition, Subtraction, Multiplication, Division
print(10 + 3)   # 13
print(10 - 3)   # 7
print(10 * 3)   # 30
print(10 / 3)   # 3.333...

# Modulo (remainder)
print(10 % 3)   # 1

# Floor division (round down)
print(10 // 3)  # 3

# Exponentiation
print(2 ** 8)   # 256
```

### Augmented Assignments

```python
x = 10
x += 5   # 15
x -= 3   # 12
x *= 2   # 24
x /= 4   # 6.0
x //= 2  # 3.0
x %= 2   # 1.0
x **= 3  # 1.0
```

### Useful Built-in Functions

```python
float(4)       # 4.0
int(4.9)       # 4
round(3.7)     # 4
abs(-13)       # 13
pow(2, 3)      # 8
bin(56)        # '0b111000'
oct(56)        # '0o70'
hex(56)        # '0x38'
```

---

## 7. Functions

```python
def get_sum(num_1, num_2):
    return num_1 + num_2

result = get_sum(3, 4)
print(result)  # 7
```

### Default Parameters

```python
def get_sum(num_1, num_2=2):
    return num_1 + num_2

get_sum(3)  # 5
```

### Return Value

If a function doesn't explicitly return, it returns `None`.

```python
def greet():
    print('hello')

result = greet()   # hello
print(result)      # None
```

### Common Built-in Functions

```python
name = input('What is your name? ')  # prompts user input
int('42')    # 42
int(True)    # 1
int(False)   # 0
```

---

## 8. Scope

```python
# Local scope — only accessible inside function
def my_func():
    num = 10

# Enclosing scope — inner function can access outer's variables
def outer():
    msg = 'Hello'
    def inner():
        print(msg)
    inner()

# Global scope — accessible from anywhere
tax = 0.70
def get_total(subtotal):
    return subtotal + (subtotal * tax)

# Built-in scope — Python's predefined functions
print(str(45))
```

---

## 9. Control Flow

### Comparison Operators

| Operator | Meaning                  |
|----------|--------------------------|
| `==`     | Equal                    |
| `!=`     | Not equal                |
| `>`      | Greater than             |
| `<`      | Less than                |
| `>=`     | Greater than or equal    |
| `<=`     | Less than or equal       |

### if / elif / else

```python
age = 16

if age >= 18:
    print('Adult')
elif age >= 13:
    print('Teenager')
else:
    print('Child')
```

### Boolean Operators

```python
# and — both must be truthy
is_citizen = True
age = 25
print(is_citizen and age >= 18)  # True

# or — at least one must be truthy
is_student = True
print(age < 18 or is_student)   # True

# not — inverts the boolean
is_admin = False
print(not is_admin)  # True
```

> `and` and `or` are **short-circuit operators** — they stop evaluating as soon as the result is determined.

---

## 10. Loops

### for Loop

```python
languages = ['Python', 'Rust', 'Java']

for lang in languages:
    print(lang)

# Looping over a string
for char in 'code':
    print(char)
```

### while Loop

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### break and continue

```python
# break — exits the loop immediately
for n in [1, 2, 3, 4]:
    if n == 3:
        break
    print(n)  # 1, 2

# continue — skips current iteration
for n in [1, 2, 3, 4]:
    if n == 3:
        continue
    print(n)  # 1, 2, 4
```

### else with Loops

The `else` block runs only if the loop was not terminated by `break`.

```python
for word in ['sky', 'rhythm']:
    for letter in word:
        if letter in 'aeiou':
            break
    else:
        print(f"'{word}' has no vowels")
```

### range()

```python
range(stop)           # 0 to stop-1
range(start, stop)    # start to stop-1
range(start, stop, step)

for num in range(2, 11, 2):
    print(num)  # 2, 4, 6, 8, 10

# Create a list from range
numbers = list(range(2, 11, 2))  # [2, 4, 6, 8, 10]
```

### enumerate() and zip()

```python
# enumerate — track index while iterating
languages = ['Spanish', 'English', 'Russian']
for index, lang in enumerate(languages):
    print(f'{index}: {lang}')

# zip — iterate over multiple iterables in parallel
names = ['Alice', 'Bob']
ids = [1, 2]
for name, id in zip(names, ids):
    print(name, id)
```

---

## 11. Lists

```python
cities = ['Los Angeles', 'London', 'Tokyo']

cities[0]    # 'Los Angeles'
cities[-1]   # 'Tokyo'
len(cities)  # 3
```

### Modifying Lists

```python
cities[0] = 'Paris'        # update
del cities[1]              # delete by index
'Tokyo' in cities          # check membership
```

### Slicing

```python
desserts = ['Cake', 'Cookies', 'Ice Cream', 'Pie']
desserts[1:3]     # ['Cookies', 'Ice Cream']
desserts[1::2]    # ['Cookies', 'Pie']
```

### Unpacking

```python
developer = ['Alice', 34, 'Rust Developer']
name, age, job = developer

# Collect remaining items
name, *rest = developer   # rest = [34, 'Rust Developer']
```

### Nested Lists

```python
developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
developer[2]      # ['Python', 'Rust', 'C++']
developer[2][1]   # 'Rust'
```

### List Methods

```python
numbers = [1, 2, 3, 4, 5]

numbers.append(6)          # add to end
numbers.extend([7, 8])     # add multiple items
numbers.insert(2, 2.5)     # insert at index
numbers.remove(5)          # remove first occurrence of value
numbers.pop(1)             # remove & return by index
numbers.pop()              # remove & return last
numbers.clear()            # remove all items
numbers.sort()             # sort in place
numbers.reverse()          # reverse in place
numbers.index('Java')      # find first index of value
sorted(numbers)            # return new sorted list (doesn't modify original)
```

---

## 12. Tuples

Tuples are **immutable** ordered collections.

```python
developer = ('Alice', 34, 'Rust Developer')
developer[1]   # 34
developer[-1]  # 'Rust Developer'
```

### Tuple Methods

```python
langs = ('Rust', 'Java', 'Python', 'Rust')

langs.count('Rust')     # 2
langs.index('Java')     # 1
sorted(langs)           # returns a new sorted list
sorted(langs, key=len)  # sort by length
sorted(langs, reverse=True)
```

### Unpacking

```python
name, age, job = developer
name, *rest = developer
```

### Tuple vs List

| Use a **List** when...            | Use a **Tuple** when...          |
|-----------------------------------|----------------------------------|
| Data needs to change              | Data is fixed and constant       |
| You need `.append()`, `.remove()` | You want immutability            |

---

## 13. Dictionaries

Collections of **key-value pairs**. Keys must be immutable.

```python
pizza = {
    'name': 'Margherita',
    'price': 8.9,
    'toppings': ['mozzarella', 'basil']
}

# Access
pizza['name']               # 'Margherita'
pizza.get('price', 0)       # 8.9 (with default fallback)
```

### Dictionary Methods

```python
pizza.keys()     # dict_keys([...])
pizza.values()   # dict_values([...])
pizza.items()    # dict_items([(...), ...])

pizza.update({'price': 10, 'size': 'large'})
pizza.pop('price', None)   # remove key, return value
pizza.popitem()            # remove last inserted item
pizza.clear()              # remove all items
```

### Looping

```python
products = {'Laptop': 990, 'Phone': 600}

for price in products.values(): ...
for product in products.keys(): ...
for product, price in products.items(): ...

# With enumerate
for index, item in enumerate(products.items(), 1):
    print(index, item)
```

---

## 14. Sets

**Unordered, mutable** collections of **unique** elements.

```python
my_set = {1, 2, 3, 4, 5}
empty_set = set()   # NOT {} — that creates a dict!
```

### Set Methods

```python
my_set.add(6)
my_set.remove(4)    # raises KeyError if not found
my_set.discard(4)   # no error if not found
my_set.clear()
```

### Set Operations

```python
a = {1, 2, 3, 4, 5}
b = {2, 3, 4, 6}

a | b   # Union:               {1, 2, 3, 4, 5, 6}
a & b   # Intersection:        {2, 3, 4}
a - b   # Difference:          {1, 5}
a ^ b   # Symmetric difference: {1, 5, 6}

b.issubset(a)     # True
a.issuperset(b)   # True
a.isdisjoint(b)   # False

5 in a            # True
```

---

## 15. List Comprehensions & Iterable Functions

### List Comprehension

```python
even_numbers = [num for num in range(21) if num % 2 == 0]
```

### filter()

```python
words = ['tree', 'sky', 'mountain', 'river', 'cloud']
long_words = list(filter(lambda w: len(w) > 4, words))
# ['mountain', 'river', 'cloud']
```

### map()

```python
celsius = [0, 10, 20, 30]
fahrenheit = list(map(lambda t: (t * 9/5) + 32, celsius))
# [32.0, 50.0, 68.0, 86.0]
```

### sum()

```python
numbers = [5, 10, 15, 20]
sum(numbers)          # 50
sum(numbers, start=10)  # 60
```

---

## 16. Lambda Functions

Anonymous, one-line functions — best used as short arguments to other functions.

```python
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4]
```

**Best practices:**
- Don't assign to a variable
- Keep them simple and readable
- Use for short, one-off functions

---

## 17. Python Standard Library & Imports

```python
import math
math.sqrt(36)   # 6.0

import math as m
m.sqrt(36)

from math import radians, sin, cos

from math import *  # Not recommended — causes naming conflicts
```

### `if __name__ == '__main__'`

```python
if __name__ == '__main__':
    # This runs only when the file is executed directly,
    # NOT when it's imported as a module
    main()
```

---

## 18. Error Handling & Exceptions

### Common Errors

| Error             | Cause                                                |
|-------------------|------------------------------------------------------|
| `SyntaxError`     | Code doesn't follow Python syntax rules              |
| `NameError`       | Variable or function not defined                     |
| `TypeError`       | Operation on incompatible types                      |
| `IndexError`      | Index out of range for a list/tuple/string           |
| `AttributeError`  | Method/property doesn't exist on the object          |

### try / except / else / finally

```python
try:
    result = 100 / int(input('Enter a number: '))
except ZeroDivisionError:
    print('Cannot divide by zero!')
except ValueError:
    print('Please enter a valid number!')
else:
    print(f'Result: {result}')   # runs if no exception
finally:
    print('Execution complete!')  # always runs
```

### Exception Object

```python
try:
    int('abc')
except ValueError as e:
    print(f'Caught: {e}')
```

### raise Statement

```python
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError('Cannot divide by zero')
    return a / b
```

### Custom Exceptions

```python
class InvalidCredentialsError(Exception):
    def __init__(self, message='Invalid username or password'):
        self.message = message
        super().__init__(self.message)

def login(username, password):
    if username != 'admin' or password != 'secret':
        raise InvalidCredentialsError()
    return f'Welcome, {username}!'
```

### Exception Chaining

```python
except FileNotFoundError:
    raise ValueError('Config file is missing') from None
except ValueError as e:
    raise ValueError('Invalid config format') from e
```

---

## 19. Object-Oriented Programming (OOP)

### Class Definition & Objects

```python
class Dog:
    species = 'French Bulldog'  # Class attribute (shared)

    def __init__(self, name, age):
        self.name = name  # Instance attribute (unique)
        self.age = age

    def bark(self):
        print(f'{self.name.upper()} says woof!')

dog1 = Dog('Jack', 3)
dog1.bark()  # JACK says woof!
```

### Dunder (Magic) Methods

```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __len__(self):     return self.pages
    def __str__(self):     return f"'{self.title}' ({self.pages} pages)"
    def __eq__(self, other): return self.pages == other.pages
```

### Encapsulation

Bundling data and methods, and hiding internal state.

```python
class Wallet:
    def __init__(self, balance):
        self.__balance = balance  # Private (double underscore)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
```

| Prefix | Convention             | Enforced? |
|--------|------------------------|-----------|
| `_x`   | Internal use           | ❌ No     |
| `__x`  | Name mangling applied  | ✅ Yes    |

### Getters, Setters & Properties

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):           # Getter
        return self._radius

    @radius.setter
    def radius(self, value):    # Setter
        if value <= 0:
            raise ValueError('Radius must be positive')
        self._radius = value

    @radius.deleter
    def radius(self):           # Deleter
        del self._radius

    @property
    def area(self):
        return 3.14 * (self._radius ** 2)
```

### Inheritance

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError

class Dog(Animal):
    def speak(self):
        return f'{self.name} says Woof!'

class Cat(Animal):
    def speak(self):
        return f'{self.name} says Meow!'
```

#### super()

```python
class GuideDog(Dog):
    def __init__(self, name, owner):
        super().__init__(name)  # Call parent's __init__
        self.owner = owner
```

#### Multiple Inheritance

```python
class GrandChild(Parent, Child):
    pass
```

### Polymorphism

Different classes sharing the same method name with different implementations.

```python
animals = [Dog('Rex'), Cat('Whiskers')]
for animal in animals:
    print(animal.speak())  # Each calls its own version
```

### Abstraction

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h
```

### Name Mangling

Python renames `__attr` to `_ClassName__attr` internally to prevent accidental override in subclasses.

```python
class Parent:
    def __init__(self):
        self.__data = 'Parent data'

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__data = 'Child data'

c = Child()
print(c.__dict__)
# {'_Parent__data': 'Parent data', '_Child__data': 'Child data'}
```

---

## 20. Algorithms & Big O Notation

**Big O** describes the worst-case growth rate of an algorithm as input size increases.

| Complexity   | Name           | Example                   |
|--------------|----------------|---------------------------|
| `O(1)`       | Constant       | Array access by index     |
| `O(log n)`   | Logarithmic    | Binary search             |
| `O(n)`       | Linear         | Iterating a list          |
| `O(n log n)` | Log-linear     | Merge sort, Quick sort    |
| `O(n²)`      | Quadratic      | Nested loops              |

### Space Complexity

- `O(1)` — constant memory regardless of input
- `O(n)` — memory grows with input size
- `O(n²)` — memory grows quadratically

### Problem-Solving Approach

1. **Understand the problem** — read carefully, identify input/output
2. **Write pseudocode** — plan before coding
3. **Consider edge cases** — boundary inputs, empty data, etc.

---

## 21. Data Structures

### Arrays (Python Lists — Dynamic)

```python
nums = [3, 4, 5, 6]
nums[0]           # O(1) access
nums.append(7)    # O(1) amortized
nums.insert(2, 9) # O(n)
nums.pop(2)       # O(n) for middle, O(1) for end
```

### Stacks (LIFO)

```python
stack = []
stack.append(1)    # Push — O(1)
stack.append(2)
top = stack.pop()  # Pop — O(1) → returns 2
```

### Queues (FIFO)

```python
from collections import deque

queue = deque()
queue.append(1)         # Enqueue — O(1)
queue.append(2)
first = queue.popleft() # Dequeue — O(1) → returns 1
```

### Linked Lists

Each node contains **data** and a **reference** to the next node.

| Operation           | Singly | Doubly |
|---------------------|--------|--------|
| Insert at beginning | O(1)   | O(1)   |
| Insert at end       | O(n)   | O(1)*  |
| Delete from start   | O(1)   | O(1)   |
| Delete from end     | O(n)   | O(1)*  |

### Hash Maps (Dictionaries)

```python
d = {'A': 1, 'B': 2}
d['A']       # O(1) avg
d['C'] = 3   # O(1) avg
del d['A']   # O(1) avg
'B' in d     # O(1) avg
```

> Worst case O(n) when hash collisions are frequent.

### When to Use What

| Structure    | Best for                                          |
|--------------|---------------------------------------------------|
| List         | Ordered, indexed access, unknown size             |
| Stack        | LIFO — undo, expression eval, backtracking        |
| Queue        | FIFO — task scheduling, BFS                       |
| Linked List  | Frequent insert/delete at start, no random access |
| Hash Map     | Fast key-value lookup, counting, caching          |
| Set          | Uniqueness, set operations, duplicate removal     |

---

## 22. Searching Algorithms

### Linear Search — O(n)

Checks each element one by one until the target is found.

```
- Time:  O(n)
- Space: O(1)
- Works on: unsorted lists
- Returns: index if found, -1 if not
```

### Binary Search — O(log n)

Divides a **sorted** list in half each step.

```
- Time:  O(log n)
- Space: O(1)
- Requires: sorted list in ascending order
- Returns: index if found, -1 if not
```

| Feature        | Linear Search | Binary Search |
|----------------|---------------|---------------|
| Requires sort  | ❌            | ✅            |
| Time           | O(n)          | O(log n)      |
| Best for       | Small lists   | Large lists   |

---

## 23. Sorting Algorithms

### Merge Sort — O(n log n)

A **divide-and-conquer** algorithm.

1. Recursively split list in half until each piece has one element
2. Merge pieces back in sorted order

```
- Time:  O(n log n)
- Space: O(n) — not in-place
```

> Python's built-in `sorted()` and `.sort()` use **Timsort**, which is also O(n log n).

---

## 24. Graphs

A set of **nodes (vertices)** connected by **edges**.

### Types

| Type         | Description                              |
|--------------|------------------------------------------|
| Directed     | Edges have direction (arrows)            |
| Undirected   | Edges have no direction                  |
| Weighted     | Edges have values (distances, costs)     |
| Cyclic       | Contains cycles                          |
| Acyclic (DAG)| No cycles                                |
| Disconnected | Some nodes not connected                 |

### Traversals

**BFS (Breadth-First Search)**
- Uses a **queue**
- Explores level by level
- Best for: shortest path in unweighted graphs

**DFS (Depth-First Search)**
- Uses a **stack** (or recursion)
- Explores a branch fully before backtracking
- Best for: cycle detection, path finding

### Representations

**Adjacency List** — space efficient for sparse graphs  
**Adjacency Matrix** — fast edge existence checks, space-heavy for large graphs

---

## 25. Trees

A **special graph** — acyclic and connected. No cycles, every node reachable.

### Binary Tree
Each node has at most **two children** (left and right).

### Binary Search Tree (BST)
- Left child < Parent
- Right child > Parent

### Trie (Prefix Tree)
- Stores strings character by character
- Shared prefixes stored once
- Used for: autocomplete, spell checking
- Search/insert: O(L) where L = string length

---

## 26. Priority Queues & Heaps

### Priority Queue
Elements served by **priority**, not insertion order.

### Heap

A tree-based structure with the **heap property**:

- **Max-Heap**: parent ≥ children (largest at root)
- **Min-Heap**: parent ≤ children (smallest at root)

```python
import heapq

heap = []
heapq.heappush(heap, 9)
heapq.heappush(heap, 3)
heapq.heappush(heap, 5)
print(heap)                  # [3, 9, 5]

print(heapq.heappop(heap))   # 3  (smallest)

# With priorities (tuple: (priority, value))
heapq.heappush(heap, (1, 'high priority'))
heapq.heappush(heap, (3, 'low priority'))
print(heapq.heappop(heap))   # (1, 'high priority')

# Convert list to heap
nums = [5, 7, 3, 1]
heapq.heapify(nums)
```

---

## 27. Dynamic Programming

Breaking a complex problem into simpler overlapping subproblems and **storing results** to avoid redundant work.

### Two Key Properties

- **Overlapping Subproblems** — same sub-problems recur multiple times
- **Optimal Substructure** — optimal solution builds on optimal sub-solutions

### Memoization (Top-Down)

```python
def climb_stairs(n, memo={}):
    if n in memo:
        return memo[n]       # Return cached result
    if n <= 2:
        return n
    memo[n] = climb_stairs(n-1, memo) + climb_stairs(n-2, memo)
    return memo[n]
```

### Tabulation (Bottom-Up)

```python
def climb_stairs(n):
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```

### When to Use DP

- Problem can be broken into overlapping subproblems
- Problem has optimal substructure
- Naive recursive solution would recalculate the same things repeatedly
- Willing to trade space for time

### Real-World Applications

- GPS shortest-path routing
- Spell checkers (edit distance)
- Financial portfolio optimization
- Resource allocation (knapsack problem)

---

*Generated from the freeCodeCamp Python Review curriculum.*