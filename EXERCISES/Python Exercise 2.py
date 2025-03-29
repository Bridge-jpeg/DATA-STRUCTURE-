user = input("Please enter your words: ").strip().lower
inp = 1
userWords = []
userWords.append(user)

while inp != 0:
    user = input("Please enter your words: ").strip().lower
    userWords.append(user)
    
    emptyList = len(userWords) = 0
    
    if (user == ""):
        inp = 0
    else: 
        inp = 1

print("Your words are: ")      
if 