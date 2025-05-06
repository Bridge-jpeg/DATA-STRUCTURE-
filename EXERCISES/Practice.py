def findSecondLargest(list):
    data_list.sort()
    print(data_list)
    if len(data_list) < 2:
        return None
    unique_numbers = set(list)
    unique_numbers.remove(max(unique_numbers))
    if len(unique_numbers) == 0:
        return None 
    return print(max(unique_numbers))

data_list = [10, 10, 10]
findSecondLargest(data_list)
