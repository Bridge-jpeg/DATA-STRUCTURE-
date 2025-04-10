stem = [0.1, 0.2, 1.0, 1.2, 2.0, 2.2, 3.3, 3.4, 3.5, 3.8, 3.7]
leaf = []
duplicates = []
seen = set()
for i in stem:
    if i in seen:
        duplicates.append(i)
    else:
        leaf.append(i)

print(duplicates.sort())
print(leaf.sort())

# set()