def simple_interest(p, t, r):
    """Calculates simple interest.

    Args:
        p: The principal amount.
        t: The time period in years.
        r: The rate of interest.

    Returns:
        The calculated simple interest.
    """

    print("The principal is:", p)
    print("The time period is:", t)
    print("The rate of interest is:", r)

    si = (p * t * r) / 100
    print("The simple interest is:", si)

    return si

# Calculate and print the simple interest for the given values
simple_interest(8, 6, 8)
