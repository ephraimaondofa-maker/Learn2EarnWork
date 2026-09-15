#Python’s lists
"""
3-1. Names: Store the names of a few of your friends in a list called names. Print
each person’s name by accessing each element in the list, one at a time.
"""
names = ['john', 'Fred', 'Annas', 'Inalegwu', 'Stephen']
print("Names of my friends: \t" + names[0].title() + ", " + names[1] + ", " + names[2] + ", " + names[3]  + ", " + names[4])

"""
3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the
person’s name.
"""
message = "I am grateful to have you as a friend "
print(message + " " + names[0].title() + " 💞💞" + " \n" + message + " " + names[1] + " 💞💞" + " \n" + message + " " + names[2] + " 💞💞" + " \n" + message + " " + names[3] + " 💞💞" + " \n" + message + " " + names[4] + " 💞💞")

"""
3-3. Your Own List: Think of your favorite mode of transportation, such as a
motorcycle or a car, and make a list that stores several examples. Use your list
to print a series of statements about these items, such as “I would like to own a
Honda motorcycle.”
"""
fruits = ['apple',  'Orange', 'Mango', 'Womanstay', 'guava']
fruits_message = "I would love to eat; "

print(fruits_message  + " " + fruits[0])
print(fruits_message  + " " + fruits[1])
print(fruits_message  + " " + fruits[2])
print(fruits_message  + " " + fruits[3])
print(fruits_message  + " " + fruits[4])

# popping items from list
last_pop = fruits.pop(3)
print(last_pop)
insertlist = fruits.insert(3, 'Womanstay')
print(fruits)

#Copying list

my_food  = ['pizza', 'falafa', 'rice', 'akpu', 'carrot cake', 'cannoli']
my_friends_food = my_food.copy()

"""
print(f"My food: {my_food}")
print(f"My friends food:  {my_friends_food}")

#Second method  using slice method
my_friends_food = my_food[:]

#Third method 
my_food = my_friends_food
"""

print(my_food)
#print(my_friends_food)
#Printing list items using slice 
print(f"The first three items in the list are:\n {my_food[:3]} ")

print(f"The last three items in the list are:\n {my_food[:5]} ")
