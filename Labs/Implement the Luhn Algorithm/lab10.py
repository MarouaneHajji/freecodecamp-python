def verify_card_number(card_number):
    """
    Verifies whether a card number is valid using the Luhn Algorithm.

    Parameters:
        card_number (str): The card number as a string (may include spaces or dashes)

    Returns:
        str: 'VALID!' if the number is valid, otherwise 'INVALID!'
    """

    # Step 1: Remove spaces and dashes
    cleaned = ""
    for char in card_number:
        if char.isdigit():
            cleaned += char

    # Step 2: Convert string to list of integers
    digits = [int(d) for d in cleaned]

    # Step 3: Apply Luhn Algorithm
    total = 0
    length = len(digits)

    # Traverse digits from right to left
    for i in range(length):
        digit = digits[length - 1 - i]

        # Double every second digit (excluding check digit)
        if i % 2 == 1:
            digit *= 2

            # If result > 9, subtract 9
            if digit > 9:
                digit -= 9

        total += digit

    # Step 4: Check if total is multiple of 10
    if total % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"


# Example tests
if __name__ == "__main__":
    print(verify_card_number('453914889'))                # VALID!
    print(verify_card_number('4111-1111-1111-1111'))      # VALID!
    print(verify_card_number('453914881'))                # INVALID!
    print(verify_card_number('1234 5678 9012 3456'))      # INVALID!