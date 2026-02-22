# Homework Problem 1
# Ask the user for two numbers.
# Print their quotient and remainder on separate lines.
user_input = float(input("give me a number"))
user_number = float(input("give me another number"))
print(user_input / user_number)
# Homework Problem 2
# Ask the user for their favorite animal and favorite color.
# Print a sentence combining them like: "A blue tiger would be awesome!"
user_animal = input("what's your favorite animal")
user_color = input("Whats your favorite color?")
print("A", user_color, user_animal, "would be cool!")


# Homework Problem 3
# Use a for loop to print all the even numbers from 0 to 10 (including 10).
numbers = ["2","4","6","8","10"]
for number in numbers:
    print(number)


# Homework Problem 4
# Ask the user how many push-ups they can do.
# Multiply it by 7 and print how many they could do in a week.
user_pushups = int(input("How much push-ups can you do?"))
print("you could do", user_pushups * 7, "push-ups in a week!")


# Homework Problem 5
# Use a for loop to print the square of each number from 1 to 6.
# (Example: 1*1=1, 2*2=4, etc.)
squares = [ 1*1, 2*2 , 3*3, 4*4, 5*5, 6*6]
for square in squares:
    print(square)