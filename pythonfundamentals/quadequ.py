"""
ROOT OF QUADRATIC EQUATION PROGRAMME  
FORMULA: root1= -b+sqrt (b*b)-(4*a*c)/(2*a)
    root2= -b-sqrt (b*b)-(4*a*c)/(2*a)
"""


print(" ☑️ " * 10 + "\tROOT OF QUADRATIC EQUATION PROGRAMME" + "  ☑️ " * 10 + " \n")
input("Press Enter to Continue ..........")

a = int(input("Enter a value.... "))
b = int(input("Enter b value.... "))
c = int(input("Enter c value.... "))

# 1. Calculate the discriminant (part under the square root)
discriminant = (b**2) - (4*a*c)

# 2. Take the square root of the discriminant
# Note: This basic version assumes the number is positive (real roots)
sqrt_val = discriminant ** 0.5

# 3. Calculate roots using correct parentheses for the numerator and denominator
root1 = (-b + sqrt_val) / (2 * a)
root2 = (-b - sqrt_val) / (2 * a)

print(f"Root 1 = {root1:.1f} | \t Root 2 = {root2:.1f}")


