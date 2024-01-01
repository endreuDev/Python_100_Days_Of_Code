print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
percentage = float(input("What percentage tip would you like to give? "
                   "10, 12, or 15? "))
split_bill = float(input("How many people to split the bill? "))
split_total = (total_bill + (percentage / 100 * total_bill)) / split_bill
print(f"Each person should pay: {round(split_total, 2)}")
