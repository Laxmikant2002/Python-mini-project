# Write a program that calculates the Body Mass Index(BMI) from a user weight

height = input("Enter Your height in m:")
# Purpose: Prompts the user to enter their height in meters and stores the input as a string in the variable height.
weight = input("Enter Your weight in kg:")
# Purpose: Prompts the user to enter their weight in kilograms and stores the input as a string in the variable weight.
bmi = int(weight)/float(height)**2
# Purpose: Calculates the Body Mass Index (BMI) using the formula: BMI = weight (kg) / height² (m²).
# int(weight): Converts the string input weight to an integer (whole number) for calculation.
# float(height): Converts the string input height to a floating-point number (decimal number) for accurate calculation.
# **2: Raises the converted height to the power of 2 (squares it).
bmi_as_int = int(bmi)
#int(bmi): Converts the bmi value to an integer, removing any decimal places.
print(bmi_as_int)

## How to check 
# if your height foot it convert meter(5 foot = 1.524 meter)
# Enter Your height in m:1.524
# Enter Your weight in kg: 50
# bmi value is : 21
# if you want to print "bmi value is : 21" then you can do this at the potion of print(bm_as_int).
# print(f"bmi value is :{bmi_as_int}")
