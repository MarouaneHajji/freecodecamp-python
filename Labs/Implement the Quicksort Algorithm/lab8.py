def quick_sort(arr):
    """
    Sorts a list of integers using the Quicksort algorithm.

    Parameters:
        arr (list): A list of integers

    Returns:
        list: A new sorted list (ascending order)
    """

    # Base case:
    # If the list has 0 or 1 element, it's already sorted
    if len(arr) <= 1:
        return arr[:]  # return a copy to avoid modifying original list

    # Step 1: Choose a pivot
    # We choose the first element (you could also choose last)
    pivot = arr[0]

    # Step 2: Partition the list into three parts
    less = []     # elements smaller than pivot
    equal = []    # elements equal to pivot
    greater = []  # elements greater than pivot

    for num in arr:
        if num < pivot:
            less.append(num)
        elif num > pivot:
            greater.append(num)
        else:
            equal.append(num)

    # Step 3: Recursively sort sublists and combine
    return quick_sort(less) + equal + quick_sort(greater)


# Example test cases
if __name__ == "__main__":
    print(quick_sort([]))  
    print(quick_sort([20, 3, 14, 1, 5]))
    print(quick_sort([83, 4, 24, 2]))
    print(quick_sort([4, 42, 16, 23, 15, 8]))
    print(quick_sort([87, 11, 23, 18, 18, 23, 11, 56, 87, 56]))