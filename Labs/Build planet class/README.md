# Build a Planet Class

## Objective

Practice Python OOP fundamentals by building a `Planet` class with input validation, instance methods, and a dunder method.

---

## What You'll Practice

- Defining a class and a constructor (`__init__`)
- Raising `TypeError` and `ValueError` for invalid input
- Assigning instance attributes (`self.name`, etc.)
- Writing instance methods that return formatted strings
- Using the `__str__` dunder method to control how objects print
- Creating instances and calling their methods

---

## File

```
planet.py
```

---

## Class Overview

### `Planet`

| Component | Purpose |
|---|---|
| `__init__(self, name, planet_type, star)` | Validates and stores the planet's data |
| `orbit()` | Returns a string describing the planet's orbit |
| `__str__()` | Controls how `print(planet)` looks |

---

## Validation Rules in `__init__`

Two layers of input checking happen before any data is stored:

**1. Type check** — all three arguments must be strings:
```python
if not isinstance(name, str) or not isinstance(planet_type, str) or not isinstance(star, str):
    raise TypeError("name, planet type, and star must be strings")
```

**2. Value check** — none of them can be an empty string:
```python
if not name or not planet_type or not star:
    raise ValueError("name, planet_type, and star must be non-empty strings")
```

---

## Method Output Format

```python
str(planet)      # "Planet: Earth | Type: Terrestrial | Star: Sun"
planet.orbit()   # "Earth is orbiting around Sun..."
```

---

## Example Usage

```python
planet_1 = Planet("Earth", "Terrestrial", "Sun")
planet_2 = Planet("Jupiter", "Gas Giant", "Sun")
planet_3 = Planet("Proxima Centauri b", "Terrestrial", "Proxima Centauri")

print(planet_1)          # Planet: Earth | Type: Terrestrial | Star: Sun
print(planet_1.orbit())  # Earth is orbiting around Sun...
```

---

## Key Concepts

**`isinstance(value, str)`** — checks whether a variable is of type `str`. More reliable than `type(value) == str` because it handles inheritance.

**`not name`** — in Python, an empty string `""` is *falsy*, so `not ""` evaluates to `True`. This is a clean way to detect empty strings without writing `name == ""`.

**`__str__`** — a dunder (magic) method. Python calls it automatically when you use `print()` or `str()` on an object. Without it, printing an object shows its memory address instead.

**`f-strings`** — `f"{self.name} is orbiting..."` embeds variable values directly into strings at runtime.

---

## Commit Message

```
feat: add Planet class with validation, orbit method, and __str__
```