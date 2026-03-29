# Problem 1
# Find and print the sum of all the numbers greater than 25 in the list.
numbers = [10, 32, 27, 8, 50]
sum = sum(numbers)
print("The sum is:", sum)


# Problem 2
# Find and print the sum of all the numbers less than -10 in the list.
numbers = [-5, -20, -11, 0, 4, -15]
total = 0
for i in range(len(numbers)):
    item = numbers[i]
    if item < -10:
        total = total + item
print("The sum of numbers less than -10 is:", total)



# Problem 3
# Find and print the biggest number less than 100 in the list.
numbers = [104, 99, 86, 120, 101]
total = 0
for i in range(len(numbers)):
    item = numbers[i]
    if item < 100 and item > total:
        total = item
print("The biggest number less than 100 is:", total)



# Problem 4
# Find and print the biggest number in the list.
numbers = [12, 7, 33, 5]
biggest = max(numbers)
print("The biggest number in the list is:", biggest)



# Problem 5
# Find and print the total sum of all the numbers in the list.
numbers = [1, 3, 5, 7, 9]
total = sum(numbers)
print("The total sum of all the numbers in the list is:", total)