# check_leap_year.py

def is_leap(year):
    # Initially, assume the year is not a leap year
    leap = False
    
    # Check if the year is evenly divisible by 400
    if year % 400 == 0: 
        leap = True
    # Check if the year is evenly divisible by 4 but not by 100
    elif year % 4 == 0 and year % 100 != 0:
        leap = True
    else:
        leap = False
    
    # Return the result
    return leap

year = int(input("Enter a year: "))
print(is_leap(year))
