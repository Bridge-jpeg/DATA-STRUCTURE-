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
my_list = [0.1, 0.0, 0.2, 2.4, 2.7, 4.2]
leaf = []
element_to_find = 1
while my_list:  
    for element in my_list:
        if element < element_to_find:
            leaf.append(element)
            element_to_find +=1
            element = my_list.pop(0)
            print(leaf)
            print(my_list)

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

nega.sort()
pos.sort()
zero.sort()

print(nega, end=" ")
print(zero, end=" ")
print(pos)
