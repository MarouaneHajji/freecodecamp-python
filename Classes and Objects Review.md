# 🐍 Python Classes and Objects

A clean reference guide covering the core concepts of Object-Oriented Programming (OOP) in Python.

---

## 📌 Table of Contents

1. [What is a Class?](#1-what-is-a-class)
2. [Creating Objects](#2-creating-objects)
3. [Attributes](#3-attributes)
4. [Methods](#4-methods)
5. [Dunder (Magic) Methods](#5-dunder-magic-methods)
6. [Real-World Example: Shopping Cart](#6-real-world-example-shopping-cart)

---

## 1. What is a Class?

A **class** is a blueprint for creating objects. It defines the behavior and data an object will have through **attributes** and **methods**.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f'{self.name.upper()} says woof woof!')
```

> **Class vs Object:** A class is a reusable template. An object is a specific instance of that class with actual data.

---

## 2. Creating Objects

Objects are created by calling the class with the required arguments.

```python
dog1 = Dog('Jack', 3)
dog2 = Dog('Thatcher', 5)

dog1.bark()  # JACK says woof woof!
dog2.bark()  # THATCHER says woof woof!
```

Methods are called on objects using **dot notation**:

```python
object_name.method_name()
```

---

## 3. Attributes

### Instance Attributes
Defined inside `__init__()` using `self`. Each object gets its own copy.

### Class Attributes
Defined directly inside the class body. Shared by **all** instances.

```python
class Dog:
    species = 'French Bulldog'  # Class attribute — shared by all dogs

    def __init__(self, name):
        self.name = name          # Instance attribute — unique per object

print(Dog.species)   # French Bulldog

jack = Dog('Jack')
print(jack.name)     # Jack
print(jack.species)  # French Bulldog (inherited from the class)
```

---

## 4. Methods

Methods are functions defined inside a class that operate on the object's attributes.

```python
class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def describe(self):
        return f'This car is a {self.color} {self.model}'

my_car_1 = Car('red', 'Tesla Model S')
my_car_2 = Car('green', 'Lamborghini Revuelto')

print(my_car_1.describe())  # This car is a red Tesla Model S
print(my_car_2.describe())  # This car is a green Lamborghini Revuelto
```

---

## 5. Dunder (Magic) Methods

**Dunder methods** (short for "double underscore") are special methods that Python calls automatically during built-in operations. They start and end with `__`.

### Common Dunder Methods

| Method | Triggered By |
|---|---|
| `__init__` | Object creation |
| `__str__` | `str()` / `print()` |
| `__len__` | `len()` |
| `__eq__` | `==` comparison |
| `__add__` | `+` operator |
| `__iter__` | `for` loop |
| `__next__` | Advancing an iterator |

### Example

```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __len__(self):
        return self.pages

    def __str__(self):
        return f"'{self.title}' has {self.pages} pages"

    def __eq__(self, other):
        return self.pages == other.pages

book1 = Book('Built Wealth Like a Boss', 420)

print(len(book1))   # 420
print(str(book1))   # 'Built Wealth Like a Boss' has 420 pages
```

> **Note:** You don't call dunder methods directly — Python calls them automatically when you use operations like `+`, `==`, `len()`, etc.

### Dunder Methods by Category

| Category | Methods |
|---|---|
| **Arithmetic** | `__add__`, `__sub__`, `__mul__`, `__truediv__` |
| **String** | `__str__`, `__repr__`, `__format__`, `__add__` |
| **Comparison** | `__eq__`, `__lt__`, `__gt__` |
| **Iteration** | `__iter__`, `__next__` |

---

## 6. Real-World Example: Shopping Cart

A practical class using multiple dunder methods to enable natural Python behavior.

```python
class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print(f'{item} is not in cart')

    def list_items(self):
        return self.items

    def __len__(self):          # Enables: len(cart)
        return len(self.items)

    def __getitem__(self, index):  # Enables: cart[0]
        return self.items[index]

    def __contains__(self, item):  # Enables: 'Laptop' in cart
        return item in self.items

    def __iter__(self):         # Enables: for item in cart
        return iter(self.items)


# Usage
cart = Cart()
cart.add('Laptop')
cart.add('Mouse')

print(len(cart))          # 2
print('Laptop' in cart)   # True
print(cart[0])            # Laptop

for item in cart:
    print(item)           # Laptop, Mouse
```

---

*Part of the Python OOP fundamentals series.*