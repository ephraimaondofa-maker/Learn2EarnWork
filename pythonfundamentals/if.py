"""
alien = ['green', 'red', 'yellow', 'white']
for alien_colour in alien:
    if alien_colour == 'green':
        print("\n You just earned 5 points.")
    elif alien_colour == 'red':
        print("\n You just earned 10 points.")
    elif alien_colour == 'yellow':
        print("\n You just earned 15 points.") 
    else:
        print("\n zero point for white")
"""
score = int(input("Enter your scores: "))

if (score >= 80) and (score<= 100):
    print("A")
    print("Excellent🤛")
elif score  >= 70 and score<= 79:
    print("B")
    print("Average")
elif score >= 60 and score<= 69:
    print("C")
    print("Keep it up 🤛")
elif score >= 50 and score<= 59:
    print("D")
    print("Work hard next time")
elif score >= 40 and score<= 49:
    print("E")
    print("Poor performance")
elif score > 0 and score <= 39:
    print("F")
else:
    print("Invalid Value")

print("\n Next term resume on 9th September, 2026")