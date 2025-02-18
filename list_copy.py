# Copying the list using deepcopy
import copy
a = [[1, 2], [3, 4], [5, 6]]
b = copy.deepcopy(a)
print(b) 

# Copying the list using list()
a = [1, 2, 3, 4, 5]
b = list(a)
print(b)


# Copying the list using slicing
a = [1, 2, 3, 4, 5]
b = a[:]
print(b)  


# Copying the list
a = [1, 2, 3, 4, 5]
b = a.copy()
print(b)
