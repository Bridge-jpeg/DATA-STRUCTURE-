list = ['awit', 'rawr', 'g', 't','j']
amen = list.count('rawr')

print(amen)
data_list = []
int_data_list = []

while True:
    given_data = input("num: ")
    if given_data != "":
        data_list.append(given_data)

    else:
        break
data_list.sort()


for item in data_list:
    int_data_list.append(int(item))
ls = [type(item) for item in int_data_list]
print(ls)

print(sum(int_data_list))