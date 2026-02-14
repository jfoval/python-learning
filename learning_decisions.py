34# Learning IF statements - Making Decisions!

# Let's check if someone can vote
age = int(input("How old are you? "))

if age >= 18:
    print("You can vote!")
    print("Don't forget to register!")
else:
    print("Sorry, you're too young to vote.")
    years_to_wait = 18 - age
    print("You need to wait", years_to_wait, "more years.")

print("")  # blank line

# Multiple conditions with elif (else-if)
print("Let's check your ticket price:")
age = int(input("Enter your age: "))

if age < 5:
    print("Ticket is FREE for toddlers!")
elif age < 18:
    print("Child ticket: $10")
elif age < 65:
    print("Adult ticket: $20")
else:
    print("Senior ticket: $15")

print("")

# Comparing things
favorite_color = input("What's your favorite color? ")

if favorite_color == "blue":
    print("Blue is my favorite too!")
if favorite_color == "pink":
    print("You are weird")
elif favorite_color == "red":
    print("Red is a bold choice!")
else:
    print(favorite_color, "is a great color!")

print("\nProgram finished!")
