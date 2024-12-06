def linear_search(arr, x):
    """Performs linear search on an array.

    Args:
        arr: The input array.
        x: The target element to search for.

    Returns:
        The index of the target element if found, otherwise -1.
    """

    n = len(arr)

    # Traverse through all elements of the array
    for i in range(n):
        if arr[i] == x:
            return i

    # If the element is not present
    return -1

# Example usage
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = linear_search(arr, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
