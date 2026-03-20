# Musical Instrument Class

## Objective

Practice Python OOP basics by building a `MusicalInstrument` class with instance attributes and methods.

---

## File

```
musical_instrument.py
```

---

## Class Overview

| Component | Description |
|---|---|
| `__init__(self, name, instrument_type)` | Stores the instrument's name and family |
| `play()` | Prints a message about playing the instrument |
| `get_fact()` | Returns a string about the instrument's family |

---

## Key Concepts

**`print` vs `return`** — `play()` uses `print()` directly, so calling it outputs text automatically. `get_fact()` uses `return`, so you need to wrap it in `print()` to see the result.

```python
instrument_1.play()                   # prints on its own
print(instrument_1.get_fact())        # needs print()
```

---
