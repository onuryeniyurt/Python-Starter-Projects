print("Welcome to the tip calculator")
bill = float(input("What was the total bill?"))
percent= int(input("How much tip would you like to give? 10, 12 or 15?"))
people= int(input("How many people to split the bill?"))

bill += (bill*percent)/100
each=round(bill/people , 2)

print(f"Each person should pay: {each}")
