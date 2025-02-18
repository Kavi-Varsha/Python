#List comprehension usage to filter even and odd numbers in the list
a = [10, 15, 23, 42, 37, 51, 62, 5]
res = [i for i in a if i % 2 != 0]
print(res)


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = [val for val in a if val % 2 == 0]
print(res)
