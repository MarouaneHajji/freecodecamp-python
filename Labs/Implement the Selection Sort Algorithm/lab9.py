def selection_sort(arr):
    """
    Sorts a list of numbers in-place using the Selection Sort algorithm.

    Parameters:
        arr (list): The list to be sorted

    Returns:
        list: The same list, sorted in ascending order
    """

    n = len(arr)

    # Loop through each position in the list
    for i in range(n):
        # Assume the current position has the minimum value
        min_index = i

        # Find the index of the smallest element in the remaining unsorted list
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap ONLY if needed (avoid unnecessary swaps)
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# Example tests
if __name__ == "__main__":
    print(selection_sort([33, 1, 89, 2, 67, 245]))
    print(selection_sort([5, 16, 99, 12, 567, 23, 15, 72, 3]))
    print(selection_sort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]))