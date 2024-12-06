# This code checks if two strings are anagrams using the Counter class from the collections module.

from collections import Counter

def check(s1, s2):
    """Checks if two strings are anagrams.

    Args:
        s1: The first string.
        s2: The second string.

    Returns:
        True if the strings are anagrams, False otherwise.
    """

    # Create Counter objects for both strings
    counter1 = Counter(s1)
    counter2 = Counter(s2)

    # Check if the character counts in both strings are equal
    if counter1 == counter2:
        return True
    else:
        return False

# Get the strings from the user (you can replace these with your own strings)
s1 = "listen"
s2 = "silent"

# Check if the strings are anagrams and print the result
if check(s1, s2):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")
