# print_sequence.py

if __name__ == '__main__':
    # Input number
    n = int(input("Enter a number: "))
    
    # Loop from 1 to n
    for i in range(1, n+1):
        # Print numbers in a sequence without newline
        print(i, end="")
