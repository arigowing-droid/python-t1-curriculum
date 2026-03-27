# Problem 1
# Count and print how many times "Alex" appears in the list.
names = ["Liam", "Alex", "Sophie", "Alex", "Mia"]
for i in range(len(names)):
    item = names[i]
    if item == "Alex":
        counter = counter + 1
print("There are", counter, "Alex appears in the list.")



# Problem 2
# Search for "elephant" in the list and print if it's found.
animals = ["zebra", "giraffe", "lion", "tiger"]
if "elephant" in animals:
    print("Elephant is found in the list.")
else:
    print("Elephant is not found in the list.")



# Problem 3
# Count and print how many scores are 100.
scores = [95, 100, 88, 100, 77, 92]

for i in range(len(scores)):
    item = scores[i]
    if item == 100:
        counter = counter + 1
print("There are", counter, "scores that are 100 in the list.")



# Problem 4
# Search for the color "blue" in the list and print its index if it's found.
colors = ["red", "green", "blue", "yellow"]
if "blue" in colors:
    index = colors.index("blue")
    print("Blue is found at index", index)
else:
    print("Blue is not found in the list.")



# Problem 5
# Count and print how many temperatures in the list are below zero.
temperatures = [3, -2, 5, -7, 0, 4, -1]
for i in range(len(temperatures)):
    item = temperatures[i]
    if item < 0:
        counter = counter + 1
print("There are", counter, "temperatures below zero in the list.")
