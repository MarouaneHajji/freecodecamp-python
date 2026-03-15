def number_pattern(n):
    # Check if the argument is an integer
    if not isinstance(n, int):
        return "Argument must be an integer value."
    
    # Check if the integer is greater than 0
    if n < 1:
        return "Argument must be an integer greater than 0."
    
    result = ""
    
    # Loop from 1 to n (included) and build the space-separated string
    for i in range(1, n + 1):
        result += str(i)
        # Add a space after each number except the last one
        if i < n:
            result += " "
    
    return result