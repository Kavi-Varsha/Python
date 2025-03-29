'''Description:
This script reads a file line by line, extracts unique words, and stores them in a list. 
It then sorts the list and prints the words in ascending order.'''



# Prompt user for file name
filename = input("Enter file name: ")
# Attempt to open the file
try:
    file_handle = open(filename, 'r')
except FileNotFoundError:
    print("File does not exist")
    quit()

# Initialize an empty list to store unique words
unique_words = []

# Process each line in the file
for line in file_handle:
    words = line.strip().split()  # Remove extra spaces and split into words
    for word in words:
        if word not in unique_words:
            unique_words.append(word)  # Add word only if it's not already in the list

# Sort the final list of words
sorted_words = sorted(unique_words)

# Print the sorted list
print(sorted_words)
