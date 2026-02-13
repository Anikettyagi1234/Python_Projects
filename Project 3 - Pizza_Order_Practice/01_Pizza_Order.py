print(" Thank you for choosing a python Pizza Delivery  ")

size = input(" Chosse a Pizza Size S, L, and M :- ")

add_pepparion = input(" DO you want a peperrion? Y or N :- ")

add_Chese = input(" DO you want exter chese? Y or N :- ")

extera_Chese = input()
S = " Small "
M = " Medium "
L = " Large "
Y = " Yes "
N = " No "
bill = 0
if size == "S" :
    bill += 15
elif size =="M" :
    bill += 20
else:
    bill += 25

if  add_pepparion == "Y" :
        if size == "S":
            bill += 2
        else:
            bill += 3
if extera_Chese == "Y" :
     bill +=1

print(f"Thanks you for Choosing Python Pizza Deliveries!\n Your Finall Bill is :- ${bill}.")