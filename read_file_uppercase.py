'''Description:
This script prompts the user for a filename, opens the file, and prints its contents in uppercase. 
It includes error handling to display a message if the file does not exist.'''

# Prompt user for file name
filename = input("Enter file name: ")

# Attempt to open the file
try:
    file_handle = open(filename, 'r')
except FileNotFoundError:
    print("File does not exist")
    quit()

# Read and print each line in uppercase
for line in file_handle:
    line = line.rstrip().upper()
    print(line)
