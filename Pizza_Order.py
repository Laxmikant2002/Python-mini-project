# Automatic Pizza order program

# Small pizza : $15
# Medium pizza : $20
# Large pizza : $25
# pepperoni for small pizza : $2
# pepperoni for medium or Large pizza : $3

print("Welcome to python pizza deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
elif size == "L":
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

if extra_cheese == "Y":
  bill += 1
  print(f"your final bill is ${bill}")