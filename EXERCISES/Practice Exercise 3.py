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
    valid_length = len(user_password) >= 8
    has_lowercase = any(char.islower() for char in user_password)
    has_uppercase = any(char.isupper() for char in user_password)
    has_digit = any(char.isdigit() for char in user_password)
    is_valid_password = has_lowercase and has_uppercase and has_digit and valid_length == True
    
    if is_valid_password:
        Pass_Value = True

    if Pass_Value == True:
        print("Your Password is Good.")
    else:
        print("Your Password is Bad, your password must contain at least one uppercase, lowercase and a number.")

user_password = input("Please enter your desired password to check: ")
check_password(user_password)

#https://www.geeksforgeeks.org/what-is-a-modulo-operator-in-python/
#https://www.geeksforgeeks.org/python-program-to-check-if-lowercase-letters-exist-in-a-string/
#https://www.geeksforgeeks.org/python-check-if-given-string-is-numeric-or-not/
#https://www.w3schools.com/python/ref_string_isdigit.asp
