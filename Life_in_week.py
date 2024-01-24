# Life in weeks 
age = int(input("waht is your current age? "))
year_remaining = 100 - age
days_remaining = year_remaining * 365
weeks_remaining = year_remaining * 52
months_remaining = year_remaining * 12

message = f"you have {days_remaining} days, {weeks_remaining} weeks,{months_remaining} months, and {year_remaining} years left"
print(message)