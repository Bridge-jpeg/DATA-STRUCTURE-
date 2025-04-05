def sample_median(given_data):
    i = 1
    data_list = []
    while True:
        if given_data != 69:
            given_data = int(input("num: "))
            data_list.append(given_data)

        else:
            break
    data_list.sort()
    if len(data_list) & 2 == 0:
        middle_median = len(data_list)/2
        median = ((data_list.index(middle_median - 1) + data_list.index(middle_median + 2)))/2
        print(median)
    else: 
        print("odd")

   


#number_terms = int(input("num: "))
choice = int(input("1or2: "))
if choice == 1:
    sample_median(choice)