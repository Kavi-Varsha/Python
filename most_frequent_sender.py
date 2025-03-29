'''Description:
This script reads a file, extracts email addresses from "From " lines, and counts occurrences using a dictionary. 
It then determines and prints the email address that appears most frequently along with its count.'''


# Prompt user for file name (default to "mbox-short.txt" if no input)
filename = input("Enter file: ").strip()
if len(filename) < 1:
    filename = "mbox-short.txt"

# Attempt to open the file
try:
    file_handle = open(filename, 'r')
except FileNotFoundError:
    print("File does not exist")
    quit()

# Dictionary to store email counts
email_counts = {}

# Process each line in the file
for line in file_handle:
    line = line.strip()
    if line.startswith("From "):  # Only consider lines starting with 'From '
        words = line.split()
        email = words[1]  # Extract email address
        email_counts[email] = email_counts.get(email, 0) + 1  # Update count

# Find the email with the highest count
most_frequent_email = None
highest_count = None

for email, count in email_counts.items():
    if most_frequent_email is None or count > highest_count:
        most_frequent_email = email
        highest_count = count

# Print the most frequent sender and their count
print(most_frequent_email, highest_count)
