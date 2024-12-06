from collections import defaultdict

# Create a defaultdict with a default value of 0
my_dict = defaultdict(int)

# Add elements to the defaultdict
my_dict['apple'] = 3
my_dict['banana'] = 2
my_dict['orange'] = 1

# Access a missing key
print(my_dict['pear'])  # Output: 0

# Update the count of an existing key
my_dict['apple'] += 2
print(my_dict)

# Iterate over the defaultdict
for key, value in my_dict.items():
    print(key, value)
