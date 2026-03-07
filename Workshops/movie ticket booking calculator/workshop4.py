# ---------------------------
# Movie Ticket Booking System
# ---------------------------

# Base information
base_price = 15
age = 21
seat_type = 'Gold'
show_time = 'Evening'

# Age eligibility
if age > 17:
    print('User is eligible to book a ticket')

# Evening show eligibility
if age >= 21:
    print('User is eligible for Evening shows')
else:
    print('User is not eligible for Evening shows')

# Membership and weekend status
is_member = True
is_weekend = False


# ---------------------------
# Membership Discount
# ---------------------------
discount = 0
if is_member and age >= 21:
    discount = 3
    print('User qualifies for membership discount')  # If conditions automatically evaluate the truthiness of 
                                                     # values—non-zero numbers, non-empty strings, and True are 
                                                     # considered truthy and trigger the if block without explicitly
                                                     # comparing to True.
else:
    print('User does not qualify for membership discount')

print('Discount:', discount)


# ---------------------------
# Extra Charges
# ---------------------------
extra_charges = 0
if is_weekend or show_time == 'Evening':
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')

print('Extra charges:', extra_charges)


# ---------------------------
# Ticket Booking Conditions
# ---------------------------
if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):  # When multiple logical operators are used in an if statement, conditions joined with and are evaluated before
                                                                      # conditions joined with or. Parentheses () are used in Python to group conditions and control the order in which
                                                                      # they are evaluated.
    print('Ticket booking condition satisfied')

    # Service charges based on seat type
    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1

    print('Service charges:', service_charges)

    # Final price calculation
    final_price = (base_price + extra_charges + service_charges) - discount
    print('Final price of ticket:', final_price)

else:
    print('Ticket booking failed due to restrictions')