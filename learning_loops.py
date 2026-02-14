# Learning LOOPS - Repeating Actions!

# FOR LOOP - Repeat a specific number of times
print("Countdown to launch!")
for i in range(5, 0, -1):  # Count from 5 down to 1
    print(i)
print("Blastoff!")
print("")

# Repeat something 10 times
print("Let's count to 10:")
for number in range(1, 11):  # range(1, 11) gives 1 to 10
    print(number)
print("")

# WHILE LOOP - Keep going until a condition is met
print("=== Number Guessing Game ===")
secret_number = 7
guess = 0

while guess != secret_number:
    guess = int(input("Guess a number between 1-10: "))

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Correct! You win!")

print("")

# Loop with a counter
print("Let's add up numbers:")
total = 0
for num in range(1, 6):  # 1, 2, 3, 4, 5
    total = total + num
    print("Adding", num, "... total so far:", total)

print("Final total:", total)
print("")

# Loop through text
name = "Python"
print("Spelling out your name:")
for letter in name:
    print(letter)

print("\nProgram finished!")
