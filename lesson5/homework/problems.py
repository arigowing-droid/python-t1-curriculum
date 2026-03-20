import random

# Problem 1
# Create a list of 3 operating systems.
# Print the last one using len().
# Then reverse the list and print it.
system = ["Windows", "macOS", "Linux"]
system.reverse()
print(system)


# Problem 2
# Create a list of 4 school subjects.
# Print the second subject.
# Then sort them alphabetically and print the result.
subjects = ["Math", "Science", "History", "English"]
subjects.sort()
print(subjects)

# Problem 3 
# Create a list of 5 error codes.
# Print how many there are.
# Then find the index of "403" and print it.
error_codes = ["404", "500", "403", "401", "502"]
print(len(error_codes))
print(error_codes.index("403"))


# Problem 4 
# Create a list of 2 programming languages.
# Print a random one.
# Then append another language and print the list.
languages = ["Python", "C++"]   
print(random.choice(languages))
languages.append("C++")
print(languages)


# Problem 5
# Create a list of 6 passwords.
# Print the one in the middle using len().
# Then remove the first password in the list and print it.
passwords = ["password", "qwertyuiop", "please enter the password", "123456", "abc123", "987654321"]
middle_index = len(passwords) // 2
print(passwords[middle_index])
first_password = passwords.pop(0)
print(first_password)
print(passwords)