def sample_median(given_data):
    i = 1
    data_list = []
    int_data_list = []
    while True:
        if given_data != "":
            given_data = input("num: ")
            data_list.append(given_data)

        else:
            break
    data_list.pop(-1)
    for item in data_list:
        int_data_list.append(int(item))
    int_data_list.sort()
    middle_median = int(len(int_data_list)/2)
    value_of_numbers = len(int_data_list) & 2 == 0 #ayaw gumana ng even and odd veryfier
    if value_of_numbers:
        print(value_of_numbers)
        print("even")
        print(int_data_list)
        even_median1 = int_data_list[middle_median - 1]
        even_median2 = int_data_list[middle_median]
        even_median = (even_median1 + even_median2)/2
        # print(middle_median)
        print(f'Median: {even_median}')
    else: 
        print(value_of_numbers)
        odd_median_index = int(middle_median + 1/2)
        print("odd")
        print(int_data_list)
        odd_median = int_data_list[odd_median_index]
        print(f'Median: {odd_median}')

# def sample_mean(given_data):

   


#number_terms = int(input("num: "))
choice = int(input("1or2: "))
if choice == 1:
    sample_median(choice)