# square_numbers.py

if __name__ == '__main__':
    # Taking an integer input from the user
    n = int(input("Enter a number: "))
    
    # Looping through the range from 0 to n-1
    for i in range(n):
        # Ensure the number is non-negative
        if i >= 0:
            # Printing the square of the current number
            print(i**2)
