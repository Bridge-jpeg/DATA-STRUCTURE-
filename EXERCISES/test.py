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

height = input("Please input your height (include if its inches or meter): ")
weight = input("Please input your weight (include if its pounds or kilogram): ")

height_value = 0
weight_value = 0
for c in height:
    if c.isdigit():
        c = int(c)
        height_value = height_value + c

for c in weight:
    if c.isdigit():
        c = int(c)
        weight_value = weight_value + c

formula1 = (weight_value / height_value * height_value) * 703
formula2 = weight_value / height_value * height_value

BMI1 = "in" or "inches" in height and "lb" or "pounds" in weight
BMI2 = "m" or "meter" in height and "kg" or "kilogram" in weight
if BMI1:
    print(f'Your BMI is {round(formula1)}')
elif BMI2:
    print(f'Your BMI is {round(formula2)}')
else:
    print("Cannot evaluate your BMI")
    

