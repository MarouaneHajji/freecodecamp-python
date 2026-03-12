# Character Creator

A Python function that creates and validates RPG characters with visual stat bars.

## Usage
```python
create_character(name, strength, intelligence, charisma)
```

## Example
```python
create_character('ren', 4, 2, 1)
```

Output:
```
ren
STR ●●●●○○○○○○
INT ●●○○○○○○○○
CHA ●○○○○○○○○○
```

## Rules

**Name**
- Must be a string
- Cannot be empty
- Max 10 characters
- No spaces allowed

**Stats**
- Must be integers
- Each stat between 1 and 4
- Total points must equal 7