# Python Dictionaries, Sets & Standard Library

A structured reference guide covering Python's built-in data structures and module system.

---

## Table of Contents

- [Dictionaries](#dictionaries)
  - [Creating Dictionaries](#creating-dictionaries)
  - [Accessing Values](#accessing-values)
  - [Common Methods](#common-dictionary-methods)
  - [Looping](#looping-over-a-dictionary)
- [Sets](#sets)
  - [Creating Sets](#creating-sets)
  - [Common Methods](#common-set-methods)
  - [Mathematical Operations](#mathematical-set-operations)
- [Python Standard Library](#python-standard-library)
  - [Import Statements](#import-statements)
  - [\_\_name\_\_ Variable](#__name__-variable)

---

## Dictionaries

Dictionaries store collections of **key-value pairs**. Keys must be **immutable** data types.

### Creating Dictionaries

**Literal syntax:**
```python
dictionary = {
    key1: value1,
    key2: value2
}
```

**`dict()` constructor** — pass a list of `(key, value)` tuples:
```python
pizza = dict([
    ('name', 'Margherita Pizza'),
    ('price', 8.9),
    ('calories_per_slice', 250),
    ('toppings', ['mozzarella', 'basil'])
])
```

---

### Accessing Values

**Bracket notation:**
```python
dictionary[key]
```

---

### Common Dictionary Methods

| Method | Description |
|--------|-------------|
| `get(key, default)` | Returns value for key; returns `default` if key doesn't exist |
| `keys()` | Returns a view of all keys |
| `values()` | Returns a view of all values |
| `items()` | Returns a view of all key-value pairs as tuples |
| `update(other_dict)` | Merges another dict in; overwrites shared keys, adds new ones |
| `pop(key, default)` | Removes and returns the value for `key`; raises `KeyError` if missing and no default |
| `popitem()` | Removes and returns the last inserted item (Python 3.7+) |
| `clear()` | Removes all key-value pairs |

```python
pizza = {'name': 'Margherita', 'price': 8.9, 'calories_per_slice': 250}

pizza.get('price', 0)           # 8.9
pizza.keys()                    # dict_keys(['name', 'price', 'calories_per_slice'])
pizza.values()                  # dict_values(['Margherita', 8.9, 250])
pizza.items()                   # dict_items([('name', 'Margherita'), ...])
pizza.update({'price': 15, 'total_time': 25})
pizza.pop('price', 10)          # returns 8.9 and removes it
pizza.popitem()                 # removes last inserted pair
pizza.clear()                   # {}
```

---

### Looping Over a Dictionary

**Values only:**
```python
for price in products.values():
    print(price)
```

**Keys only:**
```python
for product in products.keys():  # or just: for product in products
    print(product)
```

**Key-value pairs:**
```python
for product, price in products.items():
    print(product, price)
```

**With index using `enumerate()`:**
```python
# Default: starts at 0
for index, product in enumerate(products.items()):
    print(index, product)

# Custom start
for index, product in enumerate(products.items(), 1):
    print(index, product)
```

---

## Sets

Sets store **unique, unordered** values. Elements must be **immutable**. Because sets are unordered, they do not support index or key access.

### Creating Sets

```python
my_set = {1, 2, 3, 4, 5}

# Empty set — must use set(), NOT {}
empty_set = set()   # set
empty_dict = {}     # dict (not a set!)
```

---

### Common Set Methods

| Method | Description |
|--------|-------------|
| `add(elem)` | Adds an element |
| `remove(elem)` | Removes element; raises `KeyError` if not found |
| `discard(elem)` | Removes element; does nothing if not found |
| `clear()` | Removes all elements |

```python
my_set.add(6)
my_set.remove(4)     # KeyError if 4 not in set
my_set.discard(4)    # safe, no error
my_set.clear()
```

---

### Mathematical Set Operations

| Operation | Syntax | Description |
|-----------|--------|-------------|
| Union | `a \| b` | All elements from both sets |
| Intersection | `a & b` | Only elements in both |
| Difference | `a - b` | Elements in `a` not in `b` |
| Symmetric Difference | `a ^ b` | Elements in either, but not both |
| Subset check | `a.issubset(b)` | True if all of `a` is in `b` |
| Superset check | `a.issuperset(b)` | True if `a` contains all of `b` |
| Disjoint check | `a.isdisjoint(b)` | True if no elements in common |
| Membership | `x in a` | True if `x` is in the set |

```python
a = {1, 2, 3, 4, 5}
b = {2, 3, 4, 6}

a | b   # {1, 2, 3, 4, 5, 6}
a & b   # {2, 3, 4}
a - b   # {1, 5}
a ^ b   # {1, 5, 6}

b.issubset(a)    # False
a.issuperset(b)  # False

{1, 2}.isdisjoint({3, 4})  # True
5 in a                     # True
```

---

## Python Standard Library

Python ships with a large standard library of built-in modules. Import them at the top of your file.

### Import Statements

**Import the whole module:**
```python
import math
math.sqrt(36)   # 6.0
```

**Import with an alias:**
```python
import math as m
m.sqrt(36)
```

**Import specific elements:**
```python
from math import radians, sin, cos

angle = radians(40)
print(sin(angle))   # 0.6427...
print(cos(angle))   # 0.7660...
```

**Import with aliases:**
```python
from math import radians as rad, sin as sine
```

**Import everything (discouraged):**
```python
from math import *
print(sqrt(36))  # works, but risks naming conflicts
```

> ⚠️ `from module import *` makes it hard to trace where names come from and can cause conflicts. Prefer explicit imports.

---

### `__name__` Variable

`__name__` is a built-in variable Python sets automatically:

| Scenario | Value of `__name__` |
|----------|---------------------|
| File run directly | `"__main__"` |
| File imported as a module | The module's name |

Use this pattern to write code that only runs when the file is executed directly:

```python
def main():
    print("Running as main program")

if __name__ == '__main__':
    main()
```

This prevents the code inside the block from running when the file is imported elsewhere.