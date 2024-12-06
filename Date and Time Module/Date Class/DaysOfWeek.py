from datetime import date  # Import the 'date' class from the 'datetime' module

def get_day_of_week(date_obj):  # Define a function to get the day of the week for a given date object
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]  # Create a list of days of the week
    day_index = date_obj.weekday()  # Get the index of the day (0-6) from the date object
    return days[day_index]  # Return the day of the week corresponding to the index

example_date = date(2022, 1, 1)  # Create a date object for January 1, 2022
day_of_week = get_day_of_week(example_date)  # Call the function to get the day of the week for the example date

print("The day of the week for", example_date, "is", day_of_week)  # Print the result
