#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator")
bill = float(input("What is the total bill? $"))
tip = int(input("What percentage of tip? 10%, 12%, or 15%? "))
people = int(input("How many people will spilt the bill? "))

#Formula
bill_w_tip = (tip/100) * bill + bill
spilt_bill = "{0:.2f}".format(bill_w_tip / people)

print(f"Each person should pay: ${spilt_bill}")


