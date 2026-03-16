# Polygon Area Calculator

A Python OOP project implementing a `Rectangle` class and a `Square` subclass with geometric utility methods.

## Project Structure

```
shape_calculator.py   # Rectangle and Square class definitions
```

## Classes

### `Rectangle(width, height)`

Represents a rectangle. Initialized with a width and height.

| Method | Description |
|---|---|
| `set_width(w)` | Updates the width |
| `set_height(h)` | Updates the height |
| `get_area()` | Returns `width × height` |
| `get_perimeter()` | Returns `2 × (width + height)` |
| `get_diagonal()` | Returns `√(width² + height²)` |
| `get_picture()` | Returns an ASCII art grid of `*` characters |
| `get_amount_inside(shape)` | Returns how many times `shape` fits inside (no rotation) |

> `get_picture()` returns `"Too big for picture."` if width or height exceeds 50.

---

### `Square(side)` — subclass of `Rectangle`

Represents a square where width and height are always equal.

| Method | Description |
|---|---|
| `set_side(s)` | Sets both width and height to `s` |
| `set_width(w)` | Overrides parent — sets both dimensions to `w` |
| `set_height(h)` | Overrides parent — sets both dimensions to `h` |

Inherits all other methods from `Rectangle`.

---

## Usage

```python
from shape_calculator import Rectangle, Square

rect = Rectangle(10, 5)
print(rect.get_area())        # 50
rect.set_height(3)
print(rect.get_perimeter())   # 26
print(rect)                   # Rectangle(width=10, height=3)
print(rect.get_picture())
# **********
# **********
# **********

sq = Square(9)
print(sq.get_area())          # 81
sq.set_side(4)
print(sq.get_diagonal())      # 5.656854249492381
print(sq)                     # Square(side=4)
print(sq.get_picture())
# ****
# ****
# ****
# ****

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))  # 8
```

## Design Notes

- `Square` inherits all math and drawing methods from `Rectangle` with no duplication.
- Overriding `set_width` and `set_height` in `Square` ensures both dimensions stay in sync at all times.
- `get_amount_inside` uses integer division on both axes — no rotation is considered.