def divide_numbers(x, y):
  """Divides two numbers and handles potential exceptions.

  Args:
    x: The numerator.
    y: The denominator.

  Returns:
    The result of the division, or an error message if an exception occurs.
  """

  try:
    # Attempt to divide x by y
    result = x / y
  except ZeroDivisionError:
    # Handle division by zero error
    return "Division by zero error"
  except TypeError:
    # Handle invalid data type error
    return "Invalid data type"
  else:
    # Execute if no exception occurs
    return result
  finally:
    # Always execute, regardless of exceptions
    print("Division operation completed")

# Example usage:
num1 = 10
num2 = 2
result = divide_numbers(num1, num2)
print(result)  # Output: 5.0

num3 = 10
num4 = 0
result = divide_numbers(num3, num4)
print(result)  # Output: Division by zero error

num5 = "hello"
num6 = 2
result = divide_numbers(num5, num6)
print(result)  # Output: Invalid data type
