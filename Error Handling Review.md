# Python Error Handling

A reference guide covering common Python errors, debugging techniques, and exception handling patterns.

---

## Table of Contents

- [Common Errors](#common-errors)
- [Debugging Techniques](#debugging-techniques)
- [Exception Handling](#exception-handling)
- [Custom Exceptions](#custom-exceptions)
- [Exception Chaining](#exception-chaining)

---

## Common Errors

| Error | Cause | Example |
|---|---|---|
| `SyntaxError` | Code violates Python's syntax rules | `print("Hello there"` — missing closing `)` |
| `NameError` | Accessing an undefined variable or function | `print(username)` before defining `username` |
| `TypeError` | Operation on incompatible data types | Adding a string to an integer |
| `IndexError` | Accessing an out-of-range index | `greet[12]` on an 11-character string |
| `AttributeError` | Using a method/property that doesn't exist on an object | `"hello".append("!")` — strings have no `.append()` |

---

## Debugging Techniques

**1. `print()` statements**  
Insert `print()` calls at key points to inspect variable values and trace code flow.

**2. Python's built-in debugger (`pdb`)**  
Part of the standard library — no installation needed. Use `pdb.set_trace()` to pause execution and step through code interactively.

```python
import pdb
pdb.set_trace()  # Execution pauses here
```

**3. IDE debugging tools**  
Editors like PyCharm and VS Code offer breakpoints, step execution, and variable inspection panels.

---

## Exception Handling

### `try` / `except`

Wrap risky code in a `try` block. The `except` block catches a specific error if it occurs.

```python
try:
    print(22 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")
```

**Multiple `except` blocks** — chain them to handle different error types:

```python
try:
    number = int(input("Enter a number: "))
    print(22 / number)
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Please enter a valid number!")
```

---

### `else` and `finally`

- **`else`** — runs only if no exception occurred in `try`
- **`finally`** — always runs, regardless of errors

```python
try:
    result = 100 / 4
except ZeroDivisionError:
    print("You cannot divide by zero!")
else:
    print(f"Result is {result}")   # Result is 25.0
finally:
    print("Execution complete!")   # Always runs
```

---

### Exception Object (`as e`)

Access the exception itself using the `as` keyword for more detailed error messages.

```python
try:
    value = int("This will raise an error")
except ValueError as e:
    print(f"Caught an error: {e}")
    # Caught an error: invalid literal for int() with base 10: 'This will raise an error'
```

---

### `raise` Statement

Manually raise an exception when a condition is met.

```python
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("You cannot divide by zero")
    return a / b
```

---

## Custom Exceptions

Create custom exception classes by inheriting from `Exception`. Use `raise` to throw them with a custom message.

```python
class InvalidCredentialsError(Exception):
    def __init__(self, message="Invalid username or password"):
        self.message = message
        super().__init__(self.message)

def login(username, password):
    stored_username = "admin"
    stored_password = "password123"

    if username != stored_username or password != stored_password:
        raise InvalidCredentialsError()

    return f"Welcome, {username}!"
```

**Usage:**

```python
# Failed login
try:
    message = login("user", "wrongpassword")
except InvalidCredentialsError as e:
    print(f"Login failed: {e}")

# Successful login
try:
    message = login("admin", "password123")
except InvalidCredentialsError as e:
    print(f"Login failed: {e}")
else:
    print(message)  # Welcome, admin!
```

---

## Exception Chaining

Use `raise ... from` to link exceptions and show their relationship. Use `from None` to suppress the original traceback.

```python
def parse_config(filename):
    try:
        with open(filename, "r") as file:
            data = file.read()
            return int(data)
    except FileNotFoundError:
        raise ValueError("Configuration file is missing") from None
    except ValueError as e:
        raise ValueError("Invalid configuration format") from e

config = parse_config("config.txt")
```

- `from None` — hides the original exception context
- `from e` — explicitly chains to the original exception, preserving the cause