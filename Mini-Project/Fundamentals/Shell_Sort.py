def shell_sort(arr):
    # Start with a big gap size and keep reducing it by 2
    n = len(arr)
    gap = n // 2

    # Do the gap insertion sort for different gap sizes
    while gap > 0:

        # Do a gapped insertion sort for this gap size
        for i in range(gap, n):

            # Use insertion sort to sort elements
            # that are separated by gap
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp

        # Reduce the gap size by half
        gap //= 2

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
shell_sort(arr)

print("Sorted array:", arr)
