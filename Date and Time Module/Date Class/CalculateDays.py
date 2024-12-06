from datetime import date  # Import the 'date' class from the 'datetime' module

def calculate_days_between(start_date, end_date):  # Define a function to calculate days between two dates
    delta = end_date - start_date  # Calculate the difference between the two dates
    return delta.days  # Return the number of days in the difference
                       # .days is used to get only dates 
start_date = date(2022, 1, 1)  # Create a start date object
end_date = date(2022, 2, 1)  # Create an end date object

days = calculate_days_between(start_date, end_date)  # Calculate the number of days between the two dates

print("There are", days, "days between", start_date, "and", end_date)  # Print the result
