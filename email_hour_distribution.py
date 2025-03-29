'''This script reads a file, extracts the hour from timestamps in "From " lines, and counts occurrences of each hour. 
It then prints the counts sorted by hour.  From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'''

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

# Dictionary to store hour counts
hour_counts = {}

# Process each line in the file
for line in file_handle:
    line = line.strip()
    if line.startswith("From "):  # Only consider lines starting with 'From '
        words = line.split()
        time = words[5]  # Extract time (e.g., "09:14:16")
        hour = time.split(':')[0]  # Extract hour (e.g., "09")
        hour_counts[hour] = hour_counts.get(hour, 0) + 1  # Update count

# Print sorted results by hour
for hour, count in sorted(hour_counts.items()):
    print(hour, count)
