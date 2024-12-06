import datetime

# Create timedelta objects
delta1 = datetime.timedelta(days=2, hours=3)
delta2 = datetime.timedelta(hours=5, minutes=30)

# Arithmetic operations
sum_delta = delta1 + delta2
diff_delta = delta2 - delta1
multiplied_delta = delta1 * 2
divided_delta = delta2 / 2
floor_divided_delta = delta1 // 3
modulo_delta = delta1 % delta2  # Not commonly used
plus_delta = +delta1
minus_delta = -delta1
abs_delta = abs(delta2 - delta1)

# String representation
str_delta = str(delta1)
repr_delta = repr(delta1)

# Print results
print("Addition:", sum_delta)
print("Subtraction:", diff_delta)
print("Multiplication:", multiplied_delta)
print("Division:", divided_delta)
print("Floor division:", floor_divided_delta)
print("Modulo:", modulo_delta)
print("Unary plus:", plus_delta)
print("Unary minus:", minus_delta)
print("Absolute value:", abs_delta)
print("String representation:", str_delta)
print("Representation:", repr_delta)
