# Python Loops & Sequences

A comprehensive reference guide covering Python lists, tuples, loops, and related utilities.

---

## Table of Contents

1. [Lists](#lists)
2. [Tuples](#tuples)
3. [Loops](#loops)
4. [Ranges](#ranges)
5. [enumerate() and zip()](#enumerate-and-zip)
6. [List Comprehensions](#list-comprehensions)
7. [Iterable Methods](#iterable-methods)
8. [Lambda Functions](#lambda-functions)

---

## Lists

An ordered, mutable, zero-indexed sequence that can hold mixed data types.

```python
cities = ['Los Angeles', 'London', 'Tokyo']
```

### Accessing Elements

```python
cities[0]   # Los Angeles  (positive index)
cities[-1]  # Tokyo        (negative index — counts from the end)
```

### Creating a List from an Iterable

```python
list('Jessica')  # ['J', 'e', 's', 's', 'i', 'c', 'a']
```

### Common Operations

| Operation | Syntax | Notes |
|---|---|---|
| Length | `len(numbers)` | Returns number of elements |
| Update element | `lst[0] = 'new'` | Raises `IndexError` if index is out of bounds |
| Delete element | `del lst[1]` | Removes by index |
| Check membership | `'Rust' in lst` | Returns `True` or `False` |

### Slicing

```python
desserts = ['Cake', 'Cookies', 'Ice Cream', 'Pie']
desserts[1:3]    # ['Cookies', 'Ice Cream']
numbers[1::2]    # Every other element starting at index 1 → [2, 4, 6]
```

### Unpacking

```python
developer = ['Alice', 34, 'Rust Developer']
name, age, job = developer       # Exact match required
name, *rest = developer          # Collect remaining into a list
```

### Nested Lists

```python
developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
developer[2]     # ['Python', 'Rust', 'C++']
developer[2][1]  # 'Rust'
```

### List Methods

| Method | Description | Example |
|---|---|---|
| `append(x)` | Add item to end | `lst.append(6)` |
| `extend(iterable)` | Add all items from iterable | `lst.extend([6, 8, 10])` |
| `insert(i, x)` | Insert at index `i` | `lst.insert(2, 2.5)` |
| `remove(x)` | Remove first occurrence | `lst.remove(5)` |
| `pop(i)` | Remove & return item at index | `lst.pop(1)` — defaults to last |
| `clear()` | Remove all items | `lst.clear()` |
| `sort()` | Sort in place | `lst.sort()` |
| `reverse()` | Reverse in place | `lst.reverse()` |
| `index(x)` | Find first index of `x` | `lst.index('Java')` — raises `ValueError` if not found |

> **`append` vs `extend`:** `append([6, 8])` adds the list as a single nested element; `extend([6, 8])` adds each element individually.

```python
# sorted() — returns a new sorted list, original unchanged
sorted_numbers = sorted([19, 2, 35, 1])  # [1, 2, 19, 35]
```

---

## Tuples

An ordered, **immutable**, zero-indexed sequence. Use when data should not change.

```python
developer = ('Alice', 34, 'Rust Developer')
```

> **List vs Tuple:** Use a list for dynamic collections (add/remove/update). Use a tuple for fixed, read-only data.

### Accessing Elements

```python
developer[1]   # 34
numbers[-2]    # 4  (negative indexing works the same way)
```

Attempting to modify a tuple raises a `TypeError`. Attempting to access an out-of-range index raises an `IndexError`.

### Creating from an Iterable

```python
tuple('Jessica')  # ('J', 'e', 's', 's', 'i', 'c', 'a')
```

### Slicing & Unpacking

```python
desserts = ('cake', 'pie', 'cookies', 'ice cream')
desserts[1:3]          # ('pie', 'cookies')

name, age, job = developer        # Exact match required
name, *rest = developer           # Collect remaining
```

### Tuple Methods

| Method | Description | Example |
|---|---|---|
| `count(x)` | Count occurrences of `x` | `t.count('Rust')` — returns `0` if not found |
| `index(x, start?, end?)` | Find index of `x` | `t.index('Java')` — raises `ValueError` if not found |

```python
# sorted() works on tuples too — returns a new list
sorted(('Rust', 'Java', 'Python'), key=len)     # sort by length
sorted(('Rust', 'Java', 'Python'), reverse=True) # reverse alphabetical
```

---

## Loops

### `for` Loop

Iterates over any sequence (list, tuple, string, range, etc.).

```python
for language in ['Rust', 'Java', 'Python']:
    print(language)

for char in 'code':
    print(char)
```

**Nested loops:**
```python
for category in ['Fruit', 'Vegetable']:
    for food in ['Apple', 'Carrot']:
        print(category, food)
```

### `while` Loop

Repeats while the condition is `True`.

```python
secret_number = 3
guess = 0

while guess != secret_number:
    guess = int(input('Guess the number (1-5): '))
    if guess != secret_number:
        print('Wrong! Try again.')

print('You got it!')
```

### `break` and `continue`

```python
# break — exit the loop immediately
for developer in ['Jess', 'Naomi', 'Tom']:
    if developer == 'Naomi':
        break
    print(developer)   # prints 'Jess' only

# continue — skip the current iteration
for developer in ['Jess', 'Naomi', 'Tom']:
    if developer == 'Naomi':
        continue
    print(developer)   # prints 'Jess' and 'Tom'
```

### `else` Clause

The `else` block runs only when the loop completes **without** hitting a `break`.

```python
words = ['sky', 'apple', 'rhythm']

for word in words:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f"'{word}' contains the vowel '{letter}'")
            break
    else:
        print(f"'{word}' has no vowels")
```

---

## Ranges

`range(start, stop, step)` generates a sequence of integers. `stop` is **non-inclusive**.

```python
range(3)           # 0, 1, 2            (start defaults to 0)
range(2, 11, 2)    # 2, 4, 6, 8, 10    (even numbers)
range(40, 0, -10)  # 40, 30, 20, 10    (decrementing)
```

> **Notes:**
> - Requires at least one argument — no arguments raises `TypeError`
> - Only accepts integers — floats raise `TypeError`

**Convert to a list:**

```python
list(range(2, 11, 2))  # [2, 4, 6, 8, 10]
```

---

## `enumerate()` and `zip()`

### `enumerate()`

Iterates over a sequence while tracking the index.

```python
languages = ['Spanish', 'English', 'Russian']

for index, language in enumerate(languages):
    print(f'Index {index}: {language}')

# With a custom start value
for index, language in enumerate(languages, start=1):
    print(f'{index}. {language}')

# Outside a loop
list(enumerate(languages))  # [(0, 'Spanish'), (1, 'English'), (2, 'Russian')]
```

### `zip()`

Iterates over multiple iterables in parallel.

```python
developers = ['Naomi', 'Dario', 'Jessica']
ids = [1, 2, 3]

for name, id in zip(developers, ids):
    print(f'Name: {name}, ID: {id}')
```

---

## List Comprehensions

A concise way to build a list in a single line.

```python
# Syntax: [expression for item in iterable if condition]

even_numbers = [num for num in range(21) if num % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

---

## Iterable Methods

### `filter(function, iterable)`

Returns an iterator of elements that satisfy the condition.

```python
words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']

long_words = list(filter(lambda word: len(word) > 4, words))
# ['mountain', 'river', 'cloud']
```

### `map(function, iterable)`

Applies a function to every item in an iterable and returns the results.

```python
celsius = [0, 10, 20, 30, 40]

fahrenheit = list(map(lambda t: (t * 9/5) + 32, celsius))
# [32.0, 50.0, 68.0, 86.0, 104.0]
```

### `sum(iterable, start=0)`

Returns the total of all items in an iterable.

```python
numbers = [5, 10, 15, 20]

sum(numbers)         # 50
sum(numbers, 10)     # 60  (starts accumulation from 10)
sum(numbers, start=10)  # 60  (keyword argument form)
```

---

## Lambda Functions

Anonymous, single-expression functions — best used inline and kept simple.

```python
# Syntax: lambda parameters: expression

even_numbers = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))
# [2, 4]
```

**Best practices:**
- Don't assign lambdas to variables — use `def` instead for named functions
- Keep them short and readable
- Use for simple, one-off operations passed as arguments

---

## Quick Reference

| Concept | Mutable | Ordered | Indexed | Duplicates |
|---|---|---|---|---|
| List | ✅ | ✅ | ✅ | ✅ |
| Tuple | ❌ | ✅ | ✅ | ✅ |