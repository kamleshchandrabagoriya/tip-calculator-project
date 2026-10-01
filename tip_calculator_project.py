# Welcome to the tip calculator program

print("Welcome to the tip calculator program!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, 15 "))
people = int(input("How many people to split the bill? "))

bill_with_tip = (bill * tip/100) + bill
bill_per_person = bill_with_tip/people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")



# Output:

Welcome to the tip calculator program!
What was the total bill? $129.32
What percentage tip would you like to give? 10, 12, 15 15
How many people to split the bill? 5

Each person should pay: $29.74



