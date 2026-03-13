# PIN Extractor

Extracts hidden PIN codes from poems using a **diagonal word-length cipher**.

## How It Works

Each poem encodes a PIN through a simple diagonal rule:

| Line index (N) | Target word | PIN digit          |
|:--------------:|:-----------:|--------------------|
| 0              | word[0]     | length of that word |
| 1              | word[1]     | length of that word |
| 2              | word[2]     | length of that word |
| …              | word[N]     | length of that word |

If a line has **fewer words than its index requires**, the digit is `0`.

### Example

```
Stars and the moon     → line 0, word[0] = "Stars"  → 5
shine in the sky       → line 1, word[1] = "in"     → 2
white and              → line 2, word[2] = ???       → 0  (only 2 words)
until the end of night → line 3, word[3] = "of"     → 2
```
PIN: `5202`

## Usage

```python
from pin_extractor import pin_extractor

poems = [
    "Stars and the moon\nshine in the sky\nwhite and\nuntil the end of the night",
    "The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow",
    "There\nonce\nwas\na\ndragon",
]

print(pin_extractor(poems))
# → ['5202', '4323', '51110']
```

Run the demo directly:

```bash
python pin_extractor.py
```

## API

### `pin_extractor(poems: list[str]) -> list[str]`

| Parameter | Type        | Description                        |
|-----------|-------------|------------------------------------|
| `poems`   | `list[str]` | One or more multi-line poem strings |

**Returns** a `list[str]` of PIN codes, one per poem.

## File Structure

```
pin_extractor.py   # Main module + demo entry point
README.md          # This file
```
