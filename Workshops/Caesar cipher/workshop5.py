# ============================================================
# Caesar Cipher
# ============================================================
# A Caesar cipher shifts each letter in a message by a fixed
# number of positions in the alphabet.
# Example (shift=3): a → d, b → e, hello → khoor
# ============================================================

# --- HOW str.maketrans() WORKS ---
# str.maketrans(from, to) returns a dictionary mapping Unicode
# code points (integers) to Unicode code points.
# So instead of {'a': 'f', 'b': 'g', ...} you get {97: 102, ...}
# This is because str.translate() works at the codepoint level
# internally for performance.

# Quick demo:
alphabet = 'abcdefghijklmnopqrstuvwxyz'                     # all 26 lowercase letters as a reference string
shift = 5                                                    # how many positions to move each letter forward
shifted_alphabet = alphabet[shift:] + alphabet[:shift]      # rotate alphabet: 'fghijk...abcde'
translation_table = str.maketrans(alphabet, shifted_alphabet)  # map each letter to its shifted version (as unicode codepoints)

text = 'hello world'                                        # input message to encrypt
print(text.translate(translation_table))                    # apply the table to swap each letter -> mjqqt btwqi


# --- CAESAR CIPHER IMPLEMENTATION ---

def caesar(text, shift, encrypt=True):
    """Encrypt or decrypt text using the Caesar cipher."""

    if not isinstance(shift, int):                          # guard: reject non-integer shifts (e.g. '3' or 3.0)
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:                            # guard: shift must stay within the 26-letter alphabet range
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'                # reference alphabet used to build the mapping

    if not encrypt:
        shift = -shift                                      # negative shift reverses the direction -> decryption

    shifted_alphabet = alphabet[shift:] + alphabet[:shift] # build rotated alphabet based on shift value

    # Concatenate uppercase versions to handle both cases
    translation_table = str.maketrans(
        alphabet + alphabet.upper(),                        # source: all lowercase + all uppercase letters
        shifted_alphabet + shifted_alphabet.upper()         # target: their shifted counterparts, same case
    )

    return text.translate(translation_table)               # swap every letter using the table, leave non-letters untouched


def encrypt(text, shift):
    return caesar(text, shift)                             # calls caesar() with encrypt=True (default)


def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)              # calls caesar() with encrypt=False -> applies negative shift


# --- DEMO ---

encrypted = encrypt('freeCodeCamp', 3)                     # shift each letter 3 positions forward
print(f'Encrypted: {encrypted}')                           # -> iuhhFrghFdps

encrypted_text = 'Pbhentr vf sbhaq va hayvxryl cynprf.'   # pre-encrypted message using shift 13 (ROT13)
decrypted_text = decrypt(encrypted_text, 13)               # shift each letter 13 positions backward
print(f'Decrypted: {decrypted_text}')                      # -> Courage is found in unlikely places.