def distance(s1, s2):
    """Calculates the Levenshtein distance between two strings.

    Args:
        s1 (str): The first string.
        s2 (str): The second string.

    Returns:
        int: The Levenshtein distance between the two strings.
    """

    if len(s1) < len(s2):
        # If the first string is shorter, swap the strings to ensure the outer loop iterates over the longer string
        return distance(s2, s1)

    if len(s2) == 0:
        # If the second string is empty, the distance is simply the length of the first string
        return len(s1)

    # Create a matrix to store the distances between substrings
    previous_row = range(len(s2) + 1)

    for i, c1 in enumerate(s1):
        # Create a new row in the matrix
        current_row = [i + 1]

        for j, c2 in enumerate(s2):
            # Calculate the insertion, deletion, and substitution costs
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)

            # Append the minimum cost to the current row
            current_row.append(min(insertions, deletions, substitutions))

        # Update the previous row for the next iteration
        previous_row = current_row

    # Return the distance between the entire first string and the entire second string
    return previous_row[-1]


def check_plagiarism(text1, text2, threshold):
    """Checks if two text strings are similar based on a given threshold.

    Args:
        text1 (str): The first text string.
        text2 (str): The second text string.
        threshold (float): The similarity threshold (between 0 and 1).

    Returns:
        bool: True if the texts are similar, False otherwise.
    """

    # Calculate the Levenshtein distance between the two texts
    distance1 = distance(text1.lower(), text2.lower())

    # Calculate the similarity score (1 - normalized distance)
    similarity = 1 - (distance1 / max(len(text1), len(text2)))

    # Check if the similarity is above the threshold
    if similarity >= threshold:
        print("The texts are similar")
        return True
    else:
        print("The texts are not similar")
        return False
