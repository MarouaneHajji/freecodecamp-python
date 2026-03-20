# ============================================================
# ISBN VALIDATOR
# Validates whether a given ISBN-10 or ISBN-13 code is correct
# by recalculating its check digit and comparing it to the one provided.
# ============================================================


def validate_isbn(isbn, length):
    # Make sure the ISBN has exactly the right number of digits
    # (10 for ISBN-10, 13 for ISBN-13)
    if len(isbn) != length:
        print(f'ISBN-{length} code should be {length} digits long.')
        return

    # The last digit is the "check digit" — a calculated value used to verify the ISBN
    # Everything before it are the "main digits" used for the calculation
    main_digits = isbn[0:length-1]       # First 9 digits (ISBN-10) or 12 digits (ISBN-13)
    given_check_digit = isbn[length-1]   # Last digit of the ISBN the user entered

    # Convert each character in main_digits to an integer for math
    # If any character isn't a number (e.g. a hyphen), catch the error
    try:
        main_digits_list = [int(digit) for digit in main_digits]
    except ValueError:
        print('Invalid character was found.')
        return

    # Calculate what the check digit SHOULD be, based on the main digits
    if length == 10:
        expected_check_digit = calculate_check_digit_10(main_digits_list)
    else:
        expected_check_digit = calculate_check_digit_13(main_digits_list)

    # Compare the expected check digit with the one the user provided
    if given_check_digit == expected_check_digit:
        print('Valid ISBN Code.')
    else:
        print('Invalid ISBN Code.')


def calculate_check_digit_10(main_digits_list):
    # ISBN-10 check digit algorithm:
    # Multiply each of the first 9 digits by a weight from 10 down to 2,
    # sum the results, divide by 11, and subtract the remainder from 11.
    # Result 11 → '0', Result 10 → 'X', otherwise use the number as a string.
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)   # Weight decreases: 10, 9, 8 ... 2

    result = 11 - digits_sum % 11

    if result == 11:
        expected_check_digit = '0'
    elif result == 10:
        expected_check_digit = 'X'           # Special case: 'X' represents 10
    else:
        expected_check_digit = str(result)

    return expected_check_digit


def calculate_check_digit_13(main_digits_list):
    # ISBN-13 check digit algorithm:
    # Multiply digits alternately by 1 and 3, sum the results,
    # divide by 10, and subtract the remainder from 10.
    # Result 10 → '0', otherwise use the number as a string.
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit * 1          # Even positions → weight 1
        else:
            digits_sum += digit * 3          # Odd positions  → weight 3

    result = 10 - digits_sum % 10

    if result == 10:
        expected_check_digit = '0'
    else:
        expected_check_digit = str(result)

    return expected_check_digit


def main():
    user_input = input('Enter ISBN and length: ')  # e.g. "1530051126,10"

    try:
        values = user_input.split(',')  # Split on comma → ['1530051126', '10']
        isbn = values[0]                # The ISBN string
        length = int(values[1])         # The expected length as an integer
    except IndexError:
        # Triggered if the user didn't enter a comma (values[1] doesn't exist)
        print('Enter comma-separated values.')
        return
    except ValueError:
        # Triggered if the length part isn't a number (e.g. 'A')
        print('Length must be a number.')
        return

    # Only ISBN-10 and ISBN-13 are valid formats
    if length == 10 or length == 13:
        validate_isbn(isbn, length)
    else:
        print('Length should be 10 or 13.')


# main() is commented out so the test suite can import and call functions directly
# Uncomment it to run the program manually in the terminal
# main()