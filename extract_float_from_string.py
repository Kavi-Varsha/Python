'''Description:
This script extracts a floating-point number from a given string using find() and string slicing. 
It identifies the position of the number, extracts it, converts it to a float, and prints the result.'''


text = "X-DSPAM-Confidence:    0.8475"
# Find the starting position of the number
position = text.find('0.')

# Extract the number using slicing
number_string = text[position:]

# Convert to float and print
confidence_value = float(number_string)
print(confidence_value)
