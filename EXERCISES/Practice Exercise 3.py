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

# ITEM 0: Body Mass Index (BMI) 



# ITEM 1: Average 
Average_list = []
while True:
    num = int(input("Please input the numbers:"))
    if num == 0:
        break
    else:
        Average_list.append(num)

average_sum = sum(Average_list)
num_of_term = len(Average_list)
average = average_sum/num_of_term

print(average)

# ITEM 3: Negatives, Zeros, and Positives
all_numbers = []
zero = []
nega = []
pos = []
while True:
    number = input("Please input your number:")
    if number == "":
        break
    else:
        all_numbers.append(int(number))

for number in all_numbers:
    if number > 0:
        pos.append(number)
    elif number < 0:
        nega.append(number)
    else:
        zero.append(number)

print(nega, zero, pos)
