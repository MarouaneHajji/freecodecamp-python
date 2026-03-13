"""
pin_extractor.py
Extracts a secret PIN from each poem using a diagonal word-length rule:
  - On line N (0-indexed), take the word at index N and use its length as the PIN digit.
  - If the line doesn't have enough words, use '0'.
"""


def pin_extractor(poems):
    secret_codes = []

    for poem in poems:
        secret_code = ''
        lines = poem.split('\n')

        for line_index, line in enumerate(lines):
            words = line.split()

            # Diagonal rule: on line N, pick word at position N
            if len(words) > line_index:
                secret_code += str(len(words[line_index]))
            else:
                # Not enough words on this line → digit is 0
                secret_code += '0'

        secret_codes.append(secret_code)

    return secret_codes


poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
poem3 = 'There\nonce\nwas\na\ndragon'

print(pin_extractor([poem, poem2, poem3]))
