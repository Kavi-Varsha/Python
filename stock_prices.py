stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56,
                49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

def price_at(stock_prices, day):
    if 1 <= day <= 20:
        print(f"The stock price at day {day} is {stock_prices[day-1]}")
    else:
        print("Error: Day must be between 1 and 20.")

def max_at(stock_prices, day1, day2):
    if 1 <= day1 <= 20 and 1 <= day2 <= 20 and day1 <= day2:
        print(f"The max stock price between days {day1} and {day2} is {max(stock_prices[day1-1:day2])}")
    else:
        print("Error: Days must be between 1 and 20, and day1 must be less than or equal to day2.")

def min_at(stock_prices, day1, day2):
    if 1 <= day1 <= 20 and 1 <= day2 <= 20 and day1 <= day2:
        print(f"The min stock price between days {day1} and {day2} is {min(stock_prices[day1-1:day2])}")
    else:
        print("Error: Days must be between 1 and 20, and day1 must be less than or equal to day2.")

# Example calls
day = int(input("Enter the day: "))
price_at(stock_prices, day)

day1 = int(input("\nEnter the start day for max price: "))
day2 = int(input("Enter the end day for max price: "))
max_at(stock_prices, day1, day2)

day1 = int(input("\nEnter the start day for min price: "))
day2 = int(input("Enter the end day for min price: "))
min_at(stock_prices, day1, day2)
