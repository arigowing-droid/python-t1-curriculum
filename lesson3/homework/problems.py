# Problem 1
# Ask the user to enter a number.
# Print "Even" if the number is divisible by 2, otherwise print "Odd".
user_input = int(input("Enter a number."))
if user_input % 2 == 0:
    print("Even")
else:
    print("Odd")
# Problem 2
# Ask the user for the day of the week (all lowercase).
# Print "Weekend" if the day is "saturday" or "sunday",
# else print "Weekday".
user_day = input("what day is it today?")
if user_day == "saturday":
    print ("Weekend")
elif user_day == "sunday":
    print("Weekend")
else:
    print("Weekday")

# Problem 3
# Generate a random number between 1 and 10 (inclusive).
# Ask the user to guess the number.
# Print "Correct!" if the guess matches the random number, else print "Try again!".

    

# Problem 4
# Ask the user for a positive integer.
# If the number is divisible by 2 and greater than 10, print "Big even number".
# Otherwise print "Number does not meet criteria".

user_integer = int(input("Give me a positive integer"))
if user_integer % 2 == 0 and user_integer > 10:
    print("Big even number.")
else:
    print("Number does not meet criteria.")


# Problem 5
# Ask the user for two numbers.
# Print which number is larger.
# If the numbers are equal, print "Numbers are equal". 
user_num = input("Give me a number")
user_numb = input("Give me another number")
if user_num > user_numb:
    print(user_num, "is greater than", user_numb)
elif user_num < user_numb:
    print(user_numb, "is greater than", user_num)
elif user_num == user_numb:
    print("Numbers are equal.")
