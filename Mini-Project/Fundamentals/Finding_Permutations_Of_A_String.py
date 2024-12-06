from itertools import permutations

def allPermutations(str):
    """Generates all permutations of a given string.

    Args:
        str: The input string.

    Returns:
        None. The function prints all permutations of the string.
    """

    permList = permutations(str)
    for perm in list(permList):
        print(''.join(perm))

# Driver code
if __name__ == "__main__":
    str = 'ABC'
    allPermutations(str)
