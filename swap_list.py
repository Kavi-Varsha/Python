# Swap function to swap first and last element of the list
def swapList(newList):
    size = len(newList)
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp
    
    return newList
  
newList = [12, 35, 9, 56, 24]
print(swapList(newList))

#OR

my_list = [1, 2, 3, 4, 5]

# Interchange first and last elements
my_list[0], my_list[-1] = my_list[-1], my_list[0]

# Print the modified list
print("List after swapping first and last elements:", my_list)
