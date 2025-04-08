def sample_median():
    middle_median = len(int_data_list)/2
    value_of_numbers = len(int_data_list) & 2 == 0 
    if value_of_numbers:
        even_middle_median = int(middle_median - 1)
        print(value_of_numbers)
        print(f'even daw kasi {middle_median}')
        print(int_data_list)
        even_median1 = int_data_list[even_middle_median + 1]
        even_median2 = int_data_list[even_middle_median]
        even_median = (even_median1 + even_median2)/2
        print(even_middle_median)
        print(f'Median: {even_median}')
    else: 
        odd_middle_median = int(middle_median - 0.5)
        print(value_of_numbers)
        odd_median_index = int(odd_middle_median)
        print(f'odd daw kasi {middle_median}')
        print(int_data_list)
        odd_median = int_data_list[odd_median_index]
        print(f'Median: {odd_median}')

def sample_mean(given_data):
    pass

def sample_range(given_data):
    pass

def sample_variance(given_data):
    pass

def sample_standard_deviation(given_data):
    pass
   
#number_terms = int(input("num: "))
data_list = []
int_data_list = []

choice = int(input("1or2: "))
if choice == 1:
    while True:
        given_data = input("Enter 0 to start the enlisting of the data sets: ")
        if given_data != "":
            given_data = input("num: ")
            data_list.append(given_data)
        else:
            break
    data_list.remove("")
    for item in data_list:
        int_data_list.append(int(item))
    int_data_list.sort()
    sample_median(choice, data_list, int_data_list, given_data)
