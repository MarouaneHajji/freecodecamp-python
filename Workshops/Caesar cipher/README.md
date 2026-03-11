# Caesar Cipher — freeCodeCamp Python Certification Workshop

## What is a Caesar Cipher?

A **Caesar cipher** is one of the oldest and simplest encryption techniques, used by Julius Caesar to communicate secretly with his generals.

The idea is straightforward: shift every letter in a message by a fixed number of positions in the alphabet.

**Example with shift = 3:**
```
a → d    b → e    c → f    ...    z → c
hello → khoor
```

To decrypt, you just shift in the opposite direction.

---

## How the Code Works

### Core function: `caesar(text, shift, encrypt=True)`

This is the heart of the cipher. It:
1. Validates that `shift` is an integer between 1 and 25
2. Builds the shifted alphabet (e.g. with shift 3: `defg...xyzabc`)
3. Creates a translation table using `str.maketrans()` for both lowercase and uppercase letters
4. Applies the translation using `str.translate()`

```python
def caesar(text, shift, encrypt=True):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if not encrypt:
        shift = -shift
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(
        alphabet + alphabet.upper(),
        shifted_alphabet + shifted_alphabet.upper()
    )
    return text.translate(translation_table)
```

### Helper functions

```python
def encrypt(text, shift):
    return caesar(text, shift)

def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)
```

---

## Why str.maketrans()?

`str.maketrans(from, to)` builds a lookup table that maps each character's **Unicode code point** (an integer) to another code point. This is what `str.translate()` uses internally for fast character swapping.

```python
# Instead of {'a': 'f', ...} you get {97: 102, ...}
# ord('a') == 97, ord('f') == 102
```

Without it, you'd have to loop over every character manually — `maketrans` + `translate` does it in one efficient pass.

---

## Why handle uppercase separately?

Without adding uppercase mappings, letters like `C` or `A` pass through the cipher unchanged:

```python
# Without uppercase: 'freeCodeCamp' → 'iuhhCodeCamp'  ← C untouched
# With uppercase:    'freeCodeCamp' → 'iuhhFrghFdps'  ← all letters shifted
```

By concatenating `alphabet.upper()` and `shifted_alphabet.upper()` to the `maketrans` arguments, the cipher handles all letters while preserving their case.

---

## Demo

```python
# Encrypt
encrypt('freeCodeCamp', 3)     # → 'iuhhFrghFdps'

# Decrypt (ROT13 uses shift of 13)
decrypt('Pbhentr vf sbhaq va hayvxryl cynprf.', 13)
# → 'Courage is found in unlikely places.'
```

**ROT13** (shift = 13) is a special case where encrypting and decrypting use the same shift, since 13 + 13 = 26 (full alphabet cycle).

---

## Key Concepts Practiced

| Concept | Used for |
|---|---|
| Functions with default arguments | `encrypt=True` parameter |
| String slicing | Building the shifted alphabet |
| `str.maketrans()` + `str.translate()` | Efficient character substitution |
| Input validation | Checking shift type and range |
| Negative numbers | Reversing the shift to decrypt |
