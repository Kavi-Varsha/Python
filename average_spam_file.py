'''Description:
This script reads a file, extracts floating-point values from lines starting with "X-DSPAM-Confidence:", 
counts these lines, and calculates the average of the extracted values.'''

# Prompt user for file name
filename = input("Enter file name: ")

# Attempt to open the file
try:
    file_handle = open(filename, 'r')
except FileNotFoundError:
    print("File does not exist")
    quit()

# Initialize count and total variables
count = 0
total_confidence = 0

# Process each line in the file
for line in file_handle:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue  # Skip lines that don't match
    count += 1  # Count valid lines
    start_index = line.find('0.')  # Find start of the number
    confidence_value = float(line[start_index:])  # Extract and convert to float
    total_confidence += confidence_value  # Accumulate the values

# Compute and print the average
if count > 0:
    average_confidence = total_confidence / count
    print("Average spam confidence:", average_confidence)
else:
    print("No valid lines found.")
