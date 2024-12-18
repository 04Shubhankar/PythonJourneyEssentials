def binary_search(arr, x):
    """Performs binary search on a sorted array.

    Args:
        arr: The sorted input array.
        x: The target element to search for.

    Returns:
        The index of the target element if found, otherwise -1.
    """

    low = 0
    high = len(arr) - 1

    while low <= high:

        # Calculate the middle index
        mid = (low + high) // 2

        # If x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater than mid, ignore left half
        elif arr[mid] < x:
            low = mid + 1

        # If x is smaller than mid, ignore right half
        else:
            high = mid - 1

    # If we reach here, then the element was not present
    return -1

# Example usage
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binary_search(arr, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
