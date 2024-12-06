def merge_sort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        L = arr[:mid]
        R = arr[mid:]

        # Sorting the first and second halves
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # Merging the sorted halves
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Copying the remaining elements of L
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # Copying the remaining elements of R
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
merge_sort(arr)

print("Sorted array:", arr)
