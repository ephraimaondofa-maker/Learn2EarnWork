import sys

# --- Welcome Screen ---
print(" ☑️ " * 10 + "\tQUADRATIC FORMULA MATHS TUTOR" + "  ☑️ " * 10 + " \n")
print("Welcome! I won't just solve the equation; I will show you how to do it step-by-step.\n")

# --- Step 1: Suggested Inputs & Educational Context ---
print("💡 TUTOR TIP FOR BEGINNERS:")
print("To get clean, whole-number answers (no messy decimals), try these suggested values:")
print("👉 Option A:  a = 1,  b = -7,  c = 12   (Roots will be 4.0 and 3.0)")
print("👉 Option B:  a = 1,  b = -5,  c = 6    (Roots will be 3.0 and 2.0)")
print("👉 Option C:  a = 2,  b = -5,  c = 2    (Roots will be 2.0 and 0.5)\n")
print("⚠️ CRITICAL RULE: 'a' CANNOT be 0. If 'a' is 0, it is no longer a quadratic equation!")
print("-" * 65)

# --- Step 2: User Input Validation ---
a = int(input("Enter value for a: "))
if a == 0:
    print("\n❌ Error: 'a' cannot be 0. Restart the program and try a valid number.")
    sys.exit()

b = int(input("Enter value for b: "))
c = int(input("Enter value for c: "))

print("\n" + "="*25 + " TUTOR BREAKDOWN " + "="*25 + "\n")
print(f"Your Equation: ({a})x² + ({b})x + ({c}) = 0\n")

# --- Step 3: Step-by-Step Educational Output ---

# Lesson 1: The Discriminant
print("📝 STEP 1: Find the Discriminant (D = b² - 4ac)")
print(f"   Formula: D = ({b})² - (4 * {a} * {c})")

b_squared = b**2
four_ac = 4 * a * c
discriminant = b_squared - four_ac

print(f"   Calculation: D = {b_squared} - {four_ac}")
print(f"   Result: D = {discriminant}")

# Explain the nature of roots based on the discriminant
if discriminant < 0:
    print(f"   💡 Tutor Explanation: Since D ({discriminant}) is negative, this equation has NO real roots. It has complex/imaginary roots!")
    print("   (This basic tutor script handles real roots, so we will stop here to avoid errors.)")
    sys.exit()
elif discriminant == 0:
    print(f"   💡 Tutor Explanation: Since D is exactly 0, the square root of 0 is 0. This means you will get exactly ONE unique real solution.")
else:
    print(f"   💡 Tutor Explanation: Since D ({discriminant}) is positive, you will get TWO distinct real solutions.")

print("\n" + "-"*65 + "\n")

# Lesson 2: The Square Root
print("📝 STEP 2: Find the Square Root of the Discriminant (√D)")
sqrt_val = discriminant ** 0.5
print(f"   Calculation: √{discriminant} = {sqrt_val:.2f}")

print("\n" + "-"*65 + "\n")

# Lesson 3: Applying the Full Formula
print("📝 STEP 3: Plug everything into the Quadratic Formula")
print("   Formula: x = (-b ± √D) / (2a)")
print(f"   Setup:   x = (-({b}) ± {sqrt_val:.2f}) / (2 * {a})")
print(f"   Setup:   x = ({-b} ± {sqrt_val:.2f}) / {2 * a}")

print("\n" + "-"*65 + "\n")

# Lesson 4: Splitting into Two Answers
print("📝 STEP 4: Split into two paths (one for '+', one for '-')")

# Path 1: Plus
numerator1 = -b + sqrt_val
denominator = 2 * a
root1 = numerator1 / denominator
print(f"   👉 Root 1 (+) Path:")
print(f"      x1 = ({-b} + {sqrt_val:.2f}) / {denominator}")
print(f"      x1 = {numerator1} / {denominator}")
print(f"      x1 = {root1:.1f}")

print("")

# Path 2: Minus
numerator2 = -b - sqrt_val
root2 = numerator2 / denominator
print(f"   👉 Root 2 (-) Path:")
print(f"      x2 = ({-b} - {sqrt_val:.2f}) / {denominator}")
print(f"      x2 = {numerator2} / {denominator}")
print(f"      x2 = {root2:.1f}")

print("\n" + "="*20 + " END OF LESSON. HAPPY LEARNING! " + "="*20)
