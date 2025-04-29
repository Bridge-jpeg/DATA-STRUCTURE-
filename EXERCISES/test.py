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
int_data_list = [1, 2, 4, 3, 5, 6, 7, 8, 9, 10, 11]
middle_median = len(int_data_list)/2
value_of_numbers = len(int_data_list) % 2 == 0
if value_of_numbers:
    even_middle_median = int(middle_median)
    even_median1 = int_data_list[even_middle_median - 1]
    even_median2 = int_data_list[even_middle_median]
    even_median = (even_median1 + even_median2)/2
    even_median_index = int(even_median)
    even_quartile1_list = int_data_list[0 : even_median_index - 1] # quartile 1 (even)
    middle_even_quartile1 = int(len(even_quartile1_list)/2)
    even_quartile1_index1 = even_quartile1_list[middle_even_quartile1 - 1]
    even_quartile1_index2 = even_quartile1_list[middle_even_quartile1]
    even_quartile1 = (even_quartile1_index1 + even_quartile1_index2) / 2
    even_quartile3_list = int_data_list[even_median_index + 1:]
    middle_even_quartile3 = int(len(even_quartile3_list)/2)
    even_quartile3_index1 = even_quartile3_list[middle_even_quartile3- 1]
    even_quartile3_index2 = even_quartile3_list[middle_even_quartile3]
    even_quartile3 = (even_quartile3_index1 + even_quartile3_index2) / 2
    print(f'even Median: {even_median}')
    print(f"Quartile 1 (Q1): {even_quartile1}")
    print(f"Quartile 3 (Q3): {even_quartile3}")
else: 
    odd_middle_median = int(middle_median - 0.5)
    odd_median = int_data_list[odd_middle_median]
    odd_quartile1_list = int_data_list[0 : odd_median -1]
    odd_quartile1_median = len(odd_quartile1_list)/2
    odd_quartile1_index = int(odd_quartile1_median - 0.5)
    odd_quartile1 = odd_quartile1_list[odd_quartile1_index]
    odd_quartile3_list = int_data_list[odd_median:]
    odd_quartile3_median = len(odd_quartile3_list)/2
    odd_quartile3_index = int(odd_quartile3_median - 0.5)
    odd_quartile3 = odd_quartile3_list[odd_quartile3_index]
    print(f'odd Median: {odd_median}')
    print(f"Quartile 1 (Q1): {odd_quartile1}")
    print(f"Quartile 3 (Q3): {odd_quartile3}")

