# Function to sum digits of a number
def dsum(val):
    total = 0  
    while val > 0:
        total += val % 10  
        val //= 10  
    return total  

a = [123, 456, 789]
res = [dsum(val) for val in a]
print(res)
