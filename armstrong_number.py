def armstrong(num):
    # Convert the number to a string to iterate over its digits
    num_str = str(num)
    sum = 0
    # Iterate over each digit in the number
    for digit in num_str:
        sum += int(digit) ** 3

    if sum == num:
        print("It is an Armstrong number")
    else:
        print("It is not an Armstrong number")

# Input number
num = int(input("Enter a number: "))
armstrong(num)
