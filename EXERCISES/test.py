stem = []
leaf = []
duplicates = []

string_stem = str(stem)
for item in string_stem:
    duplicates.append(item)

# find = duplicates.find("0")
# ls = [type(item) for item in duplicates]
# print(ls)
# print(find)

# set()

my_list = [0.1, 0.0, 0.2, 2.4, 2.7, 4.2]
element_to_find = 1
index = -1

# for i, element in enumerate(my_list):
#     if element == element_to_find:
#         index = i
#         break

# for i, element in enumerate(my_list):
#     if element == element_to_find:
#         index = i
#         element_to_find = ++1
# cleared_list = len(my_list) != 0

# my_list = [0.1, 0.0, 0.2, 2.4, 2.7, 4.2]
# leaf = []
# element_to_find = 1
# while my_list:  
#     for element in my_list:
#         if element < element_to_find:
#             leaf.append(element)
#             element_to_find +=1
#             element = my_list.pop(0)
#             print(leaf)
#             print(my_list)

# all_numbers = []
# while True:
#     number = input("Please input your number:")
#     if number == "":
#         break
#     else:
#         all_numbers.append(int(number))

# all_numbers.sort()
# print(*all_numbers, sep = '\n')

height = input("Please input your height (include if its inches or meter): ").lower()
weight = input("Please input your weight (include if its pounds or kilogram): ").lower()

height_value = 0
weight_value = 0

for c in height:
    if c.isdigit():
        c = int(c)
        height_value += c

for c in weight:
    if c.isdigit():
        c = int(c)
        weight_value += c

print(weight)

weight_check1_BMI1 = "lb" in weight
weight_check2_BMI1 = "pounds" in weight
height_check1_BMI1 = "in" in height
height_check2_BMI1 = "inches" in height

weight_check1_BMI2 = "kg" in weight
weight_check2_BMI2 = "kilogram" in weight
height_check1_BMI2 = "m" in height
height_check2_BMI2 = "meter" in height

BMI1 = weight_check1_BMI1 or weight_check2_BMI1 and height_check1_BMI1 or height_check2_BMI1 == True
BMI2 = weight_check1_BMI2 or weight_check2_BMI2 and height_check1_BMI2 or height_check2_BMI2 == True
formula1 = ((weight_value) / (height_value * height_value)) * 703
formula2 = (weight_value) / (height_value * height_value)

if BMI1:
    print(weight_value)
    print(f'Your BMI is {round(formula1, 2)}')
elif BMI2:
    print(height_value)
    print(f'Your BMI is {round(formula2, 2)}')
else:
    print("Cannot evaluate your BMI")
    

