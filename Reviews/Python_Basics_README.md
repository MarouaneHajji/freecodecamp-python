# 🐍 Python Basics

A comprehensive reference guide covering Python fundamentals.

---

## Table of Contents

1. [What is Python?](#what-is-python)
2. [Installation](#installation)
3. [Variables](#variables)
4. [Comments & Output](#comments--output)
5. [Data Types](#data-types)
6. [Strings](#strings)
7. [Numbers & Math](#numbers--math)
8. [Functions](#functions)
9. [Scope](#scope)
10. [Comparison Operators](#comparison-operators)
11. [Conditionals](#conditionals)
12. [Boolean Logic](#boolean-logic)

---

## What is Python?

Python is a general-purpose programming language known for its simplicity and ease of use.

**Common use cases:**
- Data science & machine learning
- Web development
- Scripting & automation
- Cybersecurity
- Embedded systems (Raspberry Pi, MicroPython)

---

## Installation

Download the official installer from [python.org](https://www.python.org/) — works on Windows, Mac, and Linux.

---

## Variables

```python
name = 'John Doe'
age = 25
```

**Naming rules:**
- Must start with a letter or underscore `_`, not a number
- Can only contain letters, digits, and underscores
- Case-sensitive — `age`, `Age`, and `AGE` are all different
- Cannot use reserved keywords (`if`, `class`, `def`, etc.)
- Use `snake_case` for multi-word names

---

## Comments & Output

```python
# Single line comment

"""
Multi-line string / block comment
name = 'John Doe'
age = 25
"""

print('Hello world!')  # Hello world!
```

---

## Data Types

Python is dynamically typed — no need to declare types explicitly.

| Type | Example | Description |
|------|---------|-------------|
| `int` | `10` | Whole number |
| `float` | `4.50` | Decimal number |
| `str` | `'hello'` | Sequence of characters |
| `bool` | `True` | `True` or `False` |
| `list` | `[22, 'Hello', 3.14]` | Ordered, mutable collection |
| `tuple` | `(7, 5, 8)` | Ordered, **immutable** collection |
| `set` | `{7, 5, 8}` | Unordered, unique elements |
| `dict` | `{"name": "Alice"}` | Key-value pairs |
| `range` | `range(5)` | Sequence of numbers |
| `None` | `None` | Absence of a value |

### Mutability

- **Immutable** (cannot change): `int`, `float`, `bool`, `str`, `tuple`, `range`, `None`
- **Mutable** (can change): `list`, `set`, `dict`

### Type Checking

```python
greeting = 'Hello there!'
print(type(greeting))              # <class 'str'>
print(isinstance(greeting, str))   # True
print(isinstance(greeting, int))   # False
```

---

## Strings

```python
developer = 'Jessica'
city = "Los Angeles"
```

### Accessing Characters

```python
my_str = 'Hello world'
print(my_str[0])   # H
print(my_str[-1])  # d  (negative indexing)
```

### Escaping & Concatenation

```python
msg = 'It\'s a sunny day'

# Concatenation with +
print('My name is ' + developer + '.')

# f-strings (recommended)
greeting = f'My name is {developer}.'
```

### Slicing — `str[start:stop:step]`

```python
message = 'Python is fun!'
print(message[0:6])   # Python
print(message[7:])    # is fun!
print(message[::2])   # Pto sfn
```

### Common String Methods

```python
s = 'hello world'

s.upper()             # 'HELLO WORLD'
s.lower()             # 'hello world'
s.strip()             # removes leading/trailing whitespace
s.replace('hello', 'hi')  # 'hi world'
s.split(' ')          # ['hello', 'world']
' '.join(['a', 'b'])  # 'a b'
s.startswith('he')    # True
s.endswith('ld')      # True
s.find('world')       # 6  (-1 if not found)
s.count('l')          # 3
s.capitalize()        # 'Hello world'
s.title()             # 'Hello World'
s.isupper()           # False
s.islower()           # True
len(s)                # 11
```

---

## Numbers & Math

### Basic Operations

```python
# Addition, Subtraction, Multiplication, Division
print(56 + 12)   # 68
print(56 - 12)   # 44
print(56 * 12)   # 672
print(56 / 12)   # 4.666...

# Special operators
print(56 % 12)   # 8   — Modulo (remainder)
print(56 // 12)  # 4   — Floor division
print(4 ** 2)    # 16  — Exponentiation
```

### Augmented Assignment

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
round(3.4)     # 3
round(7.7)     # 8
abs(-13)       # 13
pow(2, 3)      # 8
bin(56)        # '0b111000'
oct(56)        # '0o70'
hex(56)        # '0x38'
```

---

## Functions

```python
def get_sum(num_1, num_2):
    return num_1 + num_2

result = get_sum(3, 4)
print(result)  # 7
```

- Functions without `return` return `None` by default
- Parameters can have default values: `def get_sum(num_1, num_2=2)`
- Calling with wrong number of arguments raises `TypeError`

### input()

```python
name = input('What is your name? ')
print('Hello', name)
```

---

## Scope

| Scope | Description |
|-------|-------------|
| **Local** | Variable inside a function — only accessible there |
| **Enclosing** | Inner function can access outer function's variables |
| **Global** | Declared outside all functions — accessible everywhere |
| **Built-in** | Python's predefined names (`print`, `type`, `len`, etc.) |

```python
# Global scope example
tax = 0.70

def get_total(subtotal):
    return subtotal + (subtotal * tax)

print(get_total(100))  # 170.0
```

---

## Comparison Operators

```python
print(3 == 4)   # False — equal
print(3 != 4)   # True  — not equal
print(3 > 4)    # False — greater than
print(3 < 4)    # True  — less than
print(3 >= 4)   # False — greater than or equal
print(3 <= 4)   # True  — less than or equal
```

---

## Conditionals

```python
age = 16

if age >= 18:
    print('You are an adult')
elif age >= 13:
    print('You are a teenager')  # ✓
else:
    print('You are a child')
```

### Nested `if`

```python
is_citizen = True
age = 25

if is_citizen:
    if age >= 18:
        print('You are eligible to vote')
```

---

## Boolean Logic

### Truthy & Falsy Values

**Falsy:** `None`, `False`, `0`, `0.0`, `''` (empty string), empty collections

**Truthy:** Non-zero numbers, non-empty strings, most other values

```python
print(bool(0))       # False
print(bool(''))      # False
print(bool(None))    # False
print(bool(1))       # True
print(bool('Hi'))    # True
```

### Boolean Operators

```python
# and — both must be truthy
is_citizen = True
age = 25
print(is_citizen and age >= 18)  # True

# or — at least one must be truthy
age = 19
is_student = True
print(age < 18 or is_student)    # True

# not — inverts the boolean value
is_admin = False
print(not is_admin)              # True
```

> **Short-circuiting:** Python evaluates `and` / `or` left to right and stops as soon as the result is determined.

---

*Happy coding! 🚀*
