# Sample list of numbers
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Initialize max and min variables
max_value = numbers[0]
min_value = numbers[0]

# Loop through the list
for number in numbers:
    if number > max_value:
        max_value = number
    if number < min_value:
        min_value = number

# Print the results
print("Maximum value:", max_value)
print("Minimum value:", min_value)


# Sample list of numbers
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Initialize max and min variables to None
maximum = None
minimum = None

# Loop through the list
for number in numbers:
    if maximum is None or number > maximum:
        maximum = number
    if minimum is None or number < minimum:
        minimum = number

# Print the results
print("Maximum value:", maximum)
print("Minimum value:", minimum)
