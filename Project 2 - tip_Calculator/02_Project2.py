print("Welcome to the tip calculator ")

bill = float(input(" Enter your bill :- $"))
tip = int(input(" How much tip would you like to give ? 10, 12, or 15 ?   "))

total_bill = bill* (1 + tip/100)

pepole = int(input(" How many people to split the bill ?"))

total_bill_per_person = total_bill / pepole

final_amount = round(total_bill_per_person, 2)

print(f" Each person should pay :- ${final_amount}\n Thanks")


