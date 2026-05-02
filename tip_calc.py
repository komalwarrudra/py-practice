bill_amount = float(input("Enter the total bill amount: $"))
tip_percentage = float(input("Enter the percentage of tip you would like to give: "))
tip_amount = bill_amount * (tip_percentage / 100)
total_amount = bill_amount + tip_amount
print(f"tip amount: ${tip_amount:.2f}")
print(f"total amount: ${total_amount:.2f}")
print("Thank you for using the tip calculator!")
split_bill = input("Would you like to split the bill? (yes/no): ").lower()
if split_bill == "yes":
    num_people = int(input("Enter the number of people to split the bill: "))
    amount_per_person = total_amount / num_people
    print(f"Each person should pay: ${amount_per_person:.2f}")