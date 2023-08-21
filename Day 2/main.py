print("Welcome to the tip calculator.")
total = float(input("What was the total bill?"))
perc = int(input("What percentage tip would you like to give? 10, 12 or 15?")) * .01
ppl = int(input("How many people to split the bill?"))
tip = total + (perc * total)
per_person = round(tip / ppl, 2)
print(f"Each person should pay: {per_person}")