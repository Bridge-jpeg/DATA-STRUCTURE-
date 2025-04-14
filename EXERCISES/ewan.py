list = ['awit', 'rawr', 'g', 't','j']
amen = list.count('rawr')

print(amen)
# data_list = []
# int_data_list = []

# while True:
#     given_data = input("num: ")
#     if given_data != "":
#         data_list.append(given_data)

#     else:
#         break
# data_list.sort()
# for item in data_list:
#     int_data_list.append(int(item))
# ls = [type(item) for item in int_data_list]
# print(ls)

# print(sum(int_data_list))

print(6**2)

my_list = [0.1, 0.0, 0.2, 2.4, 2.7, 4.2]
leaf = []
element_to_find = 1
final_element = element_to_find
my_list.sort()
largest_value = my_list[-1]

while my_list:
    element = my_list[0]  # Always look at the first element
    if element < element_to_find:
        leaf.append(element)
        element_to_find += 1
        my_list.pop(0)  # Only pop if you're using the value
        print(leaf)
        print(my_list)
    else:
        # If the current element isn't valid, move it to the end
        my_list.append(my_list.pop(0))

