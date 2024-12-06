def compound_interest(principal, rate, time):
    """Calculates compound interest.

    Args:
        principal: The principal amount.
        rate: The annual interest rate.
        time: The time period in years.

    Returns:
        The calculated compound interest.
    """

    amount = principal * (pow((1 + rate / 100), time))
    ci = amount - principal
    print("Compound interest is:", ci)

    return ci

# Calculate and print the compound interest for the given values
compound_interest(10000, 10.25, 5)
