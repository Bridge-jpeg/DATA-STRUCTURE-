list = ['awit', 'rawr', 'g', 't','j']
amen = list.count('rawr')

print(amen)
data_list = []
int_data_list = []
given_data = input("num: ")

while True:
    if given_data != "":
        given_data = input("num: ")
        data_list.append(given_data)

    else:
        break
data_list.pop(-1)
data_list.sort()

type_of_data_list = type(data_list)
print(data_list)
print(type_of_data_list)

for item in data_list:
    int_data_list.append(int(item))
ls = [type(item) for item in int_data_list]
print(ls)