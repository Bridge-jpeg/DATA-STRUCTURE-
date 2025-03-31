# Name: Lyndo M. Lusac
# Description: This program accepts input from the user and checks if the input is duplicated,
#              and prints the unique words.
# Date Submitted: March 31, 2025

user = input("Please enter your words: ")
userWords = []  # List for the words inputted by the user
isNotDupli = [] # List for the unique words 
userWords.append(user)

while user != "":
    user = input("Please enter your words: ").lower()
    userWords.append(user)

for word in userWords:      # checks the unique words
    if word.strip() not in isNotDupli:
        isNotDupli.append(word.strip())

isNotDupli.pop()    # removes the "" at the last 
print(f'Your words are: ', *isNotDupli, sep = "\n")     # prints the list of unique words