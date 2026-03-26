def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    # Negative numbers have no real square root — raise immediately
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')

    # 0 and 1 are their own square roots — handle as special cases
    if square_target in (0, 1):
        print(f'The square root of {square_target} is {square_target}')
        return square_target

    # For numbers < 1, sqrt is larger than the number itself (e.g. sqrt(0.25) = 0.5)
    # so the upper bound must be at least 1
    low = 0
    high = max(square_target, 1)

    root = None

    for _ in range(max_iterations):
        mid = (low + high) / 2

        # Check if the interval is narrow enough — this measures precision of mid itself
        if (high - low) / 2 <= tolerance:
            root = mid
            break

        # Narrow the interval toward the side that contains the true root
        if mid * mid < square_target:
            low = mid
        else:
            high = mid

    if root is None:
        print(f'Failed to converge within {max_iterations} iterations')
        return None

    print(f'The square root of {square_target} is approximately {root}')
    return root