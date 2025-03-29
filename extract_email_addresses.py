'''Description:
This script reads a file line by line, extracts and prints email addresses from lines that start with "From " (excluding "From:"). 
It also counts the number of such lines and prints the count at the end.'''

# Prompt user for file name (default to "mbox-short.txt" if no input)
filename = input("Enter file name: ").strip()
if len(filename) < 1:
    filename = "mbox-short.txt"

# Attempt to open the file
try:
    file_handle = open(filename, 'r')
except FileNotFoundError:
    print("File does not exist")
    quit()

# Initialize count variable
email_count = 0

# Process each line in the file
for line in file_handle:
    line = line.strip()
    if line.startswith("From "):  # Only consider lines starting with 'From '
        words = line.split()  # Split line into words
        print(words[1])  # Print email address (second word)
        email_count += 1  # Increase email count

# Print final count
print("There were", email_count, "lines in the file with From as the first word")
