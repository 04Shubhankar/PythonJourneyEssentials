from datetime import date

def calculate_age(birth_date):
    """Calculates the age of a person given their birth date.

    Args:
        birth_date: A date object representing the person's birth date.

    Returns:
        The person's age in years.
    """

    today = date.today()  # Get today's date
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    # The age is calculated by subtracting the birth year from the current year. The expression ((today.month, today.day) < (birth_date.month, birth_date.day)) is used to handle cases where the person's birthday hasn't passed yet in the current year. If the current date is before the birth date, 1 is subtracted from the calculated age.
    return age

birth_date = date(1990, 1, 1)  # Example birth date
age = calculate_age(birth_date)

print("The person is", age, "years old")
