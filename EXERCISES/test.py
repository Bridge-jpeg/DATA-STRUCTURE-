stem = [0.1, 0.2, 1.0, 1.2, 2.0, 2.2, 3.3, 3.4, 3.5, 3.8, 3.7]
leaf = []
duplicates = []

string_stem = str(stem)
for item in string_stem:
    duplicates.append(item)

find = duplicates.find("0")
# ls = [type(item) for item in duplicates]
# print(ls)
print(find)

# set()