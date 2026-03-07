# ---------------------------
# Bill Split Calculator
# ---------------------------

# Initial values
running_total = 0
num_of_friends = 4

# Meal costs
appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

# Calculate total bill
running_total += appetizers + main_courses + desserts + drinks
print(f'Total bill so far: {running_total}')  # Output has more decimal digits than expected, this happens because
                                              # numbers are stored in binary, and many decimal values cannot be 
                                              # represented exactly in this format, which leads to rounding errors.

# Calculate tip
tip = running_total * 0.25
print(f'Tip amount: {tip}')

# Add tip to total
running_total += tip
print(f'Total with tip: {running_total}')

# Split bill between friends
final_bill = running_total / num_of_friends
print(f'Bill per person: {final_bill}')

# Round payment per person
each_pays = round(final_bill, 2)
print(f'Each person pays: {each_pays}')