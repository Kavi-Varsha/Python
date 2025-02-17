import math

def is_fibonacci(num):
    # Function to check if a number is a perfect square
    def is_perfect_square(x):
        s = int(math.sqrt(x))
        return s * s == x

    # Check if one or both of (5 * num^2 + 4) or (5 * num^2 - 4) is a perfect square
    if is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4):
        return True
    else:
        return False

# Input number
num = int(input("Enter a number: "))
if is_fibonacci(num):
    print(f"{num} is a Fibonacci number.")
else:
    print(f"{num} is not a Fibonacci number.")
