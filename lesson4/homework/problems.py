# Problem 1
# Ask user for two test scores.
# If BOTH scores are at least 50, print "You passed both!"
# Otherwise, print "You failed at least one."
user_score = ("Enter your first test score.")
user_score2 = ("Enter your second test score.")
if user_score >= 50 and user_score2 >= 50:
    print("You passed both!")
elif user_score < 50 or user_score2 < 50:
    print("You failed at least one.")


# Problem 2
# Ask user if they brought lunch and water (yes/no).
# If they brought lunch OR water, print "You're somewhat ready."
# If they brought both, print "You're fully ready!"
# If they brought neither, print "You're not ready."
user_readiness1 = input("Did you bring lunch? (yes/no)")
user_readiness2 = input("Did you bring water? (yes/no)")
if user_readiness1 == "yes" and user_readiness2 == "yes":
    print("You're fully ready!")
elif user_readiness1 == "yes" or user_readiness2 == "yes":
    print("You're somewhat ready.")
elif user_readiness1 == "no" and user_readiness2 == "no":
    print("You're not ready.")


# Problem 3
# Ask user to enter a number.
# If the number is NOT between 1 and 10 (inclusive), print "Out of range."
# Otherwise, print "In range."
user_number = int(input("Enter a number."))
if user_number < 1 or user_number > 10:
    print("Out of range.")
else:
    print("In range.")


# Problem 4
# Generate a random number between 1 and 10.
# Ask the user to guess.
# If the guess is right AND the number is even, print "Even match!"
# Else if guess is right OR number is 5, print "Nice try!"
# Otherwise, print "Nope."
import random
num = random.randint(1, 10)
user_guess = int(input("Guess a number between 1 and 10."))
if user_guess == num and num % 2 == 0:
    print("Even match!")
elif user_guess == num or num == 5:
    print("Nice try!")
else:
    print("Nope.")



# Problem 5
# Ask the user for two numbers.
# If one is divisible by 5 AND the other is NOT divisible by 2, print "Interesting pair!"
# Otherwise, print "Plain pair."
num1 = int(input("Enter a number."))
num2 = int(input(enter another number))
if num1 or num2 % 5 and num1 or num2 % 2 != 0:
    print("Interesting pair!")
else:
    print("plain pair.")