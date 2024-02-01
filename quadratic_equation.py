# The standard form of a quadratic equation is: 𝑎𝑥^2 + 𝑏𝑥 + 𝑐 = 0
# where
# a, b and c are real numbers and
# 𝑎 ≠ 0

import math

a = float(input("Enter the Coefficient of a:"))
b = float(input("Enter the Coefficient of b:"))
c = float(input("Enter the Coefficient of c:"))

# Calculate the discriminant
discriminant = b**2 - 4*a*c

# Check the discriminant positive ,negative or zero
if discriminant > 0:
    # Real and distintct roots
    root1 = (-b + math.sqrt(discriminant))/(2*a)
    root2 = (-b - math.sqrt(discriminant))/(2*a)
    print(f"The roots are {root1} and {root2}")

elif discriminant == 0:
    # One real root(repeated)
    root = -b / (2*a)
    print(f"The root is {root}")

else:
    # Complex roots
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
    print(f"The root 1: {real_part} + {imaginary_part}i")
    print(f"The root 2: {real_part} - {imaginary_part}i")
