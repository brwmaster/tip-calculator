print("Welcome to the tip calculator")
# ask user inputs
bill = float(input("What was the total bill? €"))
percentage_tip = int(input("What percentage tip would you like to give? "))
number_of_people = int(input("How many people are spltting this bill? "))

# calculate price per person
total_bill = (bill / 100) * (100 + percentage_tip)
bill_per_person = total_bill / number_of_people
final_amount = "{:.2f}".format(bill_per_person, 2)

# print result to the user
print(f"Each person should pay: €{final_amount}")