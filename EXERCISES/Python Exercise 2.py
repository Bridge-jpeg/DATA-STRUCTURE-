user = input("Please enter your words: ")
inp = 1
userWords = []
userWords.append(user)

while inp != 0:
    userAdd = input("Please enter your words: ")
    userWords.append(userAdd)
    
    if (userAdd == ""):
        inp = 0
    else: 
        inp = 1

print("Your words are: ")      
for words in userWords:
    print(words)