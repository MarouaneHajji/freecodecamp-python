# Number Pattern Generator

A simple Python function that generates a space-separated string of integers from 1 up to a given number `n`.

## Usage
```python
number_pattern(4)   # → "1 2 3 4"
number_pattern(12)  # → "1 2 3 4 5 6 7 8 9 10 11 12"
```

## Function Signature
```python
def number_pattern(n)
```

### Parameter

| Name | Type    | Description                        |
|------|---------|------------------------------------|
| `n`  | integer | Upper bound of the pattern (inclusive) |

## Error Handling

| Input            | Return value                                  |
|------------------|-----------------------------------------------|
| Non-integer      | `Argument must be an integer value.`          |
| Integer < 1      | `Argument must be an integer greater than 0.` |

## Examples
```python
number_pattern(1)     # → "1"
number_pattern(5)     # → "1 2 3 4 5"
number_pattern(3.5)   # → "Argument must be an integer value."
number_pattern(-2)    # → "Argument must be an integer greater than 0."
number_pattern(0)     # → "Argument must be an integer greater than 0."
```

## Requirements

- Python 3.x
- No external dependencies