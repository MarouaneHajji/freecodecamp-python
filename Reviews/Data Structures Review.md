# Data Structures Review

A structured reference covering algorithms, Big O notation, and the most common data structures in Python.

---

## Table of Contents

- [Algorithms & Big O Notation](#algorithms--big-o-notation)
  - [Time Complexities](#time-complexities)
  - [Space Complexity](#space-complexity)
- [Problem-Solving Techniques](#problem-solving-techniques)
- [Arrays](#arrays)
- [Stacks](#stacks)
- [Queues](#queues)
- [Linked Lists](#linked-lists)
- [Hash Maps & Sets](#hash-maps--sets)
  - [Hash Collisions](#hash-collisions)
- [When to Use Each Data Structure](#when-to-use-each-data-structure)

---

## Algorithms & Big O Notation

**Algorithm:** A finite set of unambiguous, precise instructions for solving a problem.

**Big O Notation:** Describes the **worst-case** growth rate of an algorithm as input size increases. Ignores constants and lower-order terms — focuses on how resource usage *scales*.

---

### Time Complexities

| Notation | Name | Description |
|---|---|---|
| `O(1)` | Constant | Same time regardless of input size |
| `O(log n)` | Logarithmic | Grows slowly; input repeatedly halved (e.g. Binary Search) |
| `O(n)` | Linear | Grows proportionally to input size |
| `O(n log n)` | Log-Linear | Common in efficient sorting (Merge Sort, Quick Sort) |
| `O(n²)` | Quadratic | Grows quadratically; typical in nested loops |

#### O(1) — Constant

```python
def check_even_or_odd(number):
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'
```

#### O(n) — Linear

```python
for grade in grades:
    print(grade)
```

#### O(n²) — Quadratic

```python
for i in range(n):
    for j in range(n):
        print("Hello, World!")
```

---

### Space Complexity

| Notation | Description |
|---|---|
| `O(1)` | Constant memory regardless of input |
| `O(n)` | Memory grows proportionally with input |
| `O(n²)` | Memory grows quadratically with input |

---

## Problem-Solving Techniques

**1. Understand the Problem**
- Read the problem statement multiple times
- Identify: input → expected output → transformation needed

**2. Write Pseudocode**
High-level, language-independent logic using constructs like `IF`, `FOR`, `WHILE`:

```
GET original_string
SET reversed_string = ""
FOR EACH character IN original_string:
  ADD character TO THE BEGINNING OF reversed_string
DISPLAY reversed_string
```

**3. Handle Edge Cases**
Valid inputs at the boundaries of what the algorithm should handle. Always test for them.

---

## Arrays

| Type | Size | Notes |
|---|---|---|
| **Static Array** | Fixed at init | Elements in adjacent memory; cannot resize |
| **Dynamic Array** | Flexible | Auto-resizes by copying to a larger array |

Python lists are **dynamic arrays**.

```python
numbers = [3, 4, 5, 6]

numbers[0]          # Access → 3
numbers[2] = 16     # Update

numbers.append(7)           # Add to end
numbers.insert(3, 15)       # Insert at index

numbers.pop(2)      # Remove at index
numbers.pop()       # Remove last element
```

**Time Complexities:**

| Operation | Complexity |
|---|---|
| Access | `O(1)` |
| Insert at end | `O(1)` avg, `O(n)` when resizing |
| Insert in middle | `O(n)` |
| Delete from end | `O(1)` |
| Delete from middle | `O(n)` |

---

## Stacks

**LIFO — Last In, First Out.** Elements are added and removed from the top only.

```python
stack = []

# Push
stack.append(1)
stack.append(2)
stack.append(3)

# Pop
top = stack.pop()  # Returns 3
```

| Operation | Complexity |
|---|---|
| Push | `O(1)` |
| Pop | `O(1)` |

> **Use when:** undo functionality, expression evaluation, backtracking.

---

## Queues

**FIFO — First In, First Out.** Elements added to the back, removed from the front.

> Use `collections.deque` — Python lists are inefficient for front removal (`O(n)`).

```python
from collections import deque

queue = deque()

# Enqueue
queue.append(1)
queue.append(2)
queue.append(3)

# Dequeue
first = queue.popleft()  # Returns 1
```

| Operation | Complexity |
|---|---|
| Enqueue | `O(1)` |
| Dequeue | `O(1)` |

> **Use when:** task scheduling, breadth-first search.

---

## Linked Lists

A linear structure where each **node** holds data and a reference to the next node. Nodes are chained together — not stored in adjacent memory.

### Singly Linked List

- Each node has: `data` + reference to **next** node
- Traversal: forward only (head → tail)
- **Head:** first node (entry point)
- **Tail:** last node, points to `None`

### Doubly Linked List

- Each node has: `data` + reference to **next** and **previous** nodes
- Traversal: both directions
- Uses more memory than singly linked lists

**Time Complexities:**

| Operation | Complexity |
|---|---|
| Insert at beginning | `O(1)` |
| Insert at end / middle | `O(n)` |
| Delete from beginning | `O(1)` |
| Delete from end / middle | `O(n)` |

> **Use when:** frequent insertion/deletion at the beginning, size unknown, random access not needed.

---

## Hash Maps & Sets

### Hash Maps (Dictionaries)

A **Map** is an abstract data type that stores **key-value pairs** — every key is unique, values can repeat.

A **Hash Map** implements this using a hash function to convert keys into array indices.

```python
my_dict = {"A": 1, "B": 2, "C": 3}
my_dict = dict(A=1, B=2, C=3)  # Alternative

# Access & modify
my_dict["A"]        # 1
my_dict["A"] = 4    # Update
del my_dict["A"]    # Remove

# Membership
"C" in my_dict

# Views
my_dict.keys()
my_dict.values()
my_dict.items()
```

**Time Complexities:**

| Operation | Average | Worst Case |
|---|---|---|
| Insert / Get / Delete | `O(1)` | `O(n)` (collisions) |

---

### Sets

Unordered collections of **unique, immutable** elements. No duplicates, no guaranteed order.

> Use `set()` for an empty set — `{}` creates an empty dict.

```python
numbers = {1, 2, 3, 4}
empty_set = set()

# Add & remove
numbers.add(5)
numbers.remove(4)    # Raises KeyError if missing
numbers.discard(4)   # Silent if missing

# Set operations
a = {1, 2, 3, 4}
b = {2, 3, 4, 5, 6}

a | b   # Union
a & b   # Intersection
a - b   # Difference
a ^ b   # Symmetric difference

# Relationship checks
a.issubset(b)
a.issuperset(b)
a.isdisjoint(b)

# Membership
5 in numbers
```

**Time Complexities:**

| Operation | Average | Worst Case |
|---|---|---|
| Add / Remove / Membership | `O(1)` | `O(n)` (collisions) |

---

### Hash Collisions

Occurs when two different keys produce the same hash value.

| Strategy | How it works |
|---|---|
| **Chaining** | Each index holds a linked list of all colliding elements |
| **Open Addressing** | Searches for the next available index using a predefined sequence |

---

## When to Use Each Data Structure

| Data Structure | Best For |
|---|---|
| **List** | Ordered, indexed access; size unknown in advance |
| **Stack** | LIFO operations — undo, expression evaluation, backtracking |
| **Queue** | FIFO operations — task scheduling, BFS |
| **Linked List** | Frequent insertion/deletion at the start; no random access needed |
| **Hash Map** | Fast key-value lookups, counting occurrences, caching |
| **Set** | Uniqueness checking, set operations, removing duplicates |