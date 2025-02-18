a = [10, 20, 30, 40, 50]
totalSum = 0
length = 0

# Finding sum using a loop
for val in a:
    totalSum += val
    length += 1

average = totalSum / length if a else 0  # Avoid division by zero

print("Sum of the list:", totalSum)
print("Average of the list:", average)
