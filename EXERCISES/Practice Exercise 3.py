#Author: Lyndo M. Lusac 
#Description: This program ask the user for a password and checks whether the password is good or bad. It's good if the 
#             input contains at least one uppercase, lowercase and a number, if not then it is bad.
#Date of submission: April 4, 2025
#ID number: 2024-140342
X = 140342
item_number = int(X%4)
print(f'Your item number is {item_number}.')

def check_password(user_password):
    Pass_Value = False
    if len(user_password) >= 8:
        has_lowercase = any(char.islower() for char in user_password)
        has_uppercase = any(char.isupper() for char in user_password)
        if has_lowercase and has_uppercase == True:
            for char in user_password:
                if char.isdigit():
                    Pass_Value = True
        else:
            Pass_Value = False
    else:
        Pass_Value = False

    if Pass_Value == True:
        print("Your Password is Good.")
    else:
        print("Your Password is Bad, your password must contain at least one uppercase, lowercase and a number.")

user_password = input("Please enter your desired password to check: ")
check_password(user_password)



