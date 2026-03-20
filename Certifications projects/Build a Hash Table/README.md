# Hash Table — Python Implementation

A Hash Table built from scratch in Python as part of the freeCodeCamp Python certification curriculum.

---

## What is a Hash Table?

A **hash table** is a data structure that stores **key-value pairs**. Instead of storing keys directly, it first runs the key through a **hash function** that converts it into a numeric index. That index is then used to store and retrieve the value — making lookups extremely fast.

```
Key ("golf")  →  Hash Function  →  424  →  { 'golf': 'sport' }
```

---

## How This Implementation Works

### Storage Structure

Internally, the table uses a **nested dictionary**:

```python
{
    hash_value: { original_key: value, ... },
    ...
}
```

### Hash Function

The hash is computed by summing the **Unicode value** of every character in the key using Python's built-in `ord()` function.

```python
hash('golf') → ord('g') + ord('o') + ord('l') + ord('f')
             → 103 + 111 + 108 + 102 = 424
```

### Collision Handling

Two different keys can sometimes produce the **same hash value** (this is called a **collision**). For example, `'dear'` and `'read'` both hash to `412` because they contain the same characters.

When a collision occurs, both key-value pairs are stored **together inside the same bucket** (nested dict):

```python
{ 412: { 'dear': 'friend', 'read': 'book' } }
```

---

## Class: `HashTable`

### `hash(key)` → `int`
Converts a string key into a numeric hash value.

```python
ht = HashTable()
ht.hash('golf')  # returns 424
```

### `add(key, value)`
Stores a key-value pair in the table. Handles collisions automatically.

```python
ht.add('golf', 'sport')
# collection → { 424: { 'golf': 'sport' } }

ht.add('fcc', 'coding')
ht.add('cfc', 'chemical')
# collection → { 300: { 'fcc': 'coding', 'cfc': 'chemical' } }
```

### `lookup(key)` → `value` or `None`
Returns the value for a given key, or `None` if the key doesn't exist.

```python
ht.lookup('golf')   # returns 'sport'
ht.lookup('piano')  # returns None
```

### `remove(key)`
Removes a specific key-value pair. Safe to call with a non-existent key — no error is raised.

```python
ht.remove('golf')
ht.lookup('golf')   # now returns None
```

---

## Quick Example

```python
ht = HashTable()

ht.add('rose', 'flower')
ht.add('golf', 'sport')
ht.add('fcc', 'coding')
ht.add('cfc', 'chemical')   # collision with 'fcc'

print(ht.lookup('rose'))    # flower
print(ht.lookup('golf'))    # sport
print(ht.lookup('fcc'))     # coding
print(ht.lookup('cfc'))     # chemical

ht.remove('golf')
print(ht.lookup('golf'))    # None
```

---

## Files

| File | Description |
|------|-------------|
| `hash_table.py` | Hash Table class with full comments |

---

## Concepts Covered

- Hash functions and Unicode values (`ord()`)
- Collision handling with nested dictionaries
- Class design with `__init__` and instance methods
- Safe key lookup and deletion patterns