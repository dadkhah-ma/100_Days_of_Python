# tip calculator

print("Welcome to the tip calculator")

total_bill = float(input("What was the total bill? $"))
tip_percentage = float(input("What percentage tip would you like to give?  "))
people_count = int(input("How many people to split the bill? "))

total_bill_add_tip = total_bill * ((tip_percentage / 100) + 1)
people_share = round(total_bill_add_tip / people_count, 2)
people_share = "{:.2f}".format(people_share)

print(f"Each person should pay: ${people_share}")
