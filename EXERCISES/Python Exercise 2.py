user = input("Please enter your words: ")
userWords = []
isNotDupli = []
userWords.append(user.lower())

while user != "":
    user = input("Please enter your words: ")
    userWords.append(user.lower())

for word in userWords:
    if word.strip() not in isNotDupli:
        isNotDupli.append(word.strip())

isNotDupli.pop()
print(f'Your words are: ', *isNotDupli, sep = "\n")

# references:
# sep()
# not
# * 