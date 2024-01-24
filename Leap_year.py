# Leap year checking

# How work out the whether if a particular year is a leap year
#1- on every year that is evenly divided by 4
#2- Except every year that is evenly divided by 4
#3- Unless the year is also evenly divided by 400

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")