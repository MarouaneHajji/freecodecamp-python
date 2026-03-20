# Object-Oriented Programming (OOP) Review

A summary of the four key OOP principles in Python: **Encapsulation**, **Inheritance**, **Polymorphism**, and **Abstraction**.

---

## Table of Contents

- [What is OOP?](#what-is-oop)
- [Encapsulation](#encapsulation)
  - [Getters, Setters & Deleters](#getters-setters--deleters)
- [Inheritance](#inheritance)
- [Polymorphism](#polymorphism)
- [Name Mangling](#name-mangling)
- [Abstraction](#abstraction)

---

## What is OOP?

**Object-Oriented Programming (OOP)** is a programming style where developers model code around real-world objects.

| Concept | Description |
|---|---|
| **Class** | A blueprint for creating objects |
| **Object** | An instance of a class with attributes (data) and methods (behavior) |

The four key principles are: **Encapsulation**, **Inheritance**, **Polymorphism**, and **Abstraction**.

---

## Encapsulation

Bundling attributes and methods into a single unit, and hiding internal state behind a public interface.

- **Single underscore** `_attr` → convention for internal use (not enforced)
- **Double underscore** `__attr` → name mangling; effectively prevents external access

```python
class Wallet:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

account = Wallet(500)
print(account.__balance)  # AttributeError: no attribute '__balance'
```

---

### Getters, Setters & Deleters

**Properties** connect getters and setters to attributes, allowing dot-notation access with logic running behind the scenes.

#### Getter — `@property`

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def area(self):
        return 3.14 * (self._radius ** 2)

my_circle = Circle(3)
print(my_circle.radius)  # 3
print(my_circle.area)    # 28.26
```

#### Setter — `@<property>.setter`

> ⚠️ Always store the value in an internal attribute (e.g. `self._radius`), never assign to the property name itself — that causes a `RecursionError`.

```python
@radius.setter
def radius(self, value):
    if value <= 0:
        raise ValueError('Radius must be positive')
    self._radius = value

my_circle.radius = 8  # Calls the setter
```

#### Deleter — `@<property>.deleter`

```python
@radius.deleter
def radius(self):
    print("Deleting radius...")
    del self._radius

del my_circle.radius  # Calls the deleter
```

#### How Python calls them automatically

```python
my_circle.radius      # → calls getter
my_circle.radius = 4  # → calls setter
del my_circle.radius  # → calls deleter
```

---

## Inheritance

A child class reuses the attributes and methods of a parent class.

```python
class Parent:
    pass

class Child(Parent):  # Single inheritance
    pass

class GrandChild(Parent, Child):  # Multiple inheritance
    pass
```

Use `super()` to call a parent method without duplicating code:

```python
class Child(Parent):
    def __init__(self):
        super().__init__()  # Calls Parent's __init__
```

---

## Polymorphism

Different classes share the same method name but each implements it differently.

```python
class A:
    def action(self): ...

class B:
    def action(self): ...

class C:
    def action(self): ...

# Works for A, B, or C — same interface, different behavior
instance.action()
```

**Inheritance-based polymorphism:** a parent defines a method, and each child overrides it with its own implementation.

---

## Name Mangling

When you prefix an attribute with `__`, Python internally renames it to `_ClassName__attribute`. This prevents accidental overriding in subclasses.

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

Both attributes coexist safely without collision.

---

## Abstraction

Hides complex implementation details and exposes only the essential interface. Implemented via the `abc` module.

| Term | Description |
|---|---|
| `ABC` | Abstract Base Class — cannot be instantiated directly |
| `@abstractmethod` | Must be overridden in every subclass |

```python
from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

class ConcreteClassOne(AbstractClass):
    def abstract_method(self):
        print('Implementation in ConcreteClassOne')

class ConcreteClassTwo(AbstractClass):
    def abstract_method(self):
        print('Implementation in ConcreteClassTwo')
```

> **Real-world analogy:** A car exposes the wheel, pedals, and shifter — you don't need to know how the engine or brakes work internally.