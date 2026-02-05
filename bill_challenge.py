bill = input("How much was the bill? ")
bill_value = int(bill)

Service = input("How was your meal? ")
if Service == "bad":
    tip = 1.0
if Service == "okay":
    tip = 1.15
if Service == "good":
    tip = 1.20
if Service == "great":
    tip = 1.25

print('Great to hear! Your meal is $', bill_value * tip)
