def squareIt(x):
  """Calculates the square of a number.

  Args:
    x: The number to be squared.

  Returns:
    The square of the input number.
  """

  return x ** x

# Assert statements to verify the correctness of the squareIt function
assert squareIt(2) == 4, "The Square of 2 should be 4"
assert squareIt(3) == 9, "The square of 3 should be 9"
assert squareIt(4) == 16, "The square of 4 should be 16"

# Print the results of the squareIt function for different inputs
print(squareIt(2))
print(squareIt(3))
print(squareIt(4))


"""

Explanation:

def squareIt(x):: Defines a function named squareIt that takes a single argument x.
return x ** x: Calculates the square of x by raising it to the power of itself and returns the result.
assert squareIt(2) == 4, "The Square of 2 should be 4": Asserts that the square of 2 is equal to 4. If the assertion fails, an AssertionError is raised with the given message.
assert squareIt(3) == 9, "The square of 3 should be 9": Asserts that the square of 3 is equal to 9. If the assertion fails, an AssertionError is raised with the given message.
assert squareIt(4) == 16, "The square of 4 should be 16": Asserts that the square of 4 is equal to 16. If the assertion fails, an AssertionError is raised with the given message.
print(squareIt(2)): Prints the result of calling squareIt with the argument 2.
print(squareIt(3)): Prints the result of calling squareIt with the argument 3.
print(squareIt(4)): Prints the result of calling squareIt with the argument 4.
"""
