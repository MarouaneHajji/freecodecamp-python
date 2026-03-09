def apply_discount(price, discount):
    if not isinstance(price, (int, float)):
        return "The price should be a number"
    
    if not isinstance(discount, (int, float)):
        return "The discount should be a number"
    
    if price <= 0:
        return "The price should be greater than 0"
    
    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"
    
    discount_amount = price * (discount / 100)
    final_price = price - discount_amount
    return final_price


print(apply_discount(50, 20))


# Use elif when you have multiple mutually exclusive conditions that must be checked in sequence but without returning immediately.

# Use separate ifs when each condition can exit the function early, like in validation checks.