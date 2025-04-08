def sample_median(int_data_list):
    middle_median = len(int_data_list)/2
    value_of_numbers = len(int_data_list) & 2 == 0 
    if value_of_numbers:
        even_middle_median = int(middle_median - 1)
        # print(value_of_numbers)
        # print(f'even daw kasi {middle_median}')
        # print(int_data_list)
        even_median1 = int_data_list[even_middle_median + 1]
        even_median2 = int_data_list[even_middle_median]
        even_median = (even_median1 + even_median2)/2
        # print(even_middle_median)
        print(f'Median: {even_median}')
    else: 
        odd_middle_median = int(middle_median - 0.5)
        # print(value_of_numbers)
        odd_median_index = int(odd_middle_median)
        # print(f'odd daw kasi {middle_median}')
        # print(int_data_list)
        odd_median = int_data_list[odd_median_index]
        print(f'Median: {odd_median}')

def sample_mean(int_data_list, n_terms):
    sum_of_data = sum(int_data_list)
    mean = (sum_of_data)/n_terms
    print(f'Mean: {mean}')

def trimmed_mean(trimmed_input, int_data_list, n_terms):
    trimmed_decimal = trimmed_input/100
    formula_for_trimmed = int((trimmed_decimal)*(len(int_data_list)))
    trimmed_datalist = int_data_list[formula_for_trimmed: -formula_for_trimmed]
    sum_of_trimmed_data = sum(int_data_list)
    trimmed_formula = (sum_of_trimmed_data)/n_terms
    # trimmed_data_list = int_data_list.pop(int_data_list[formula_for_trimmed: -1])
    print(f'Trimmed Data list: {trimmed_datalist} \nTrimmed Mean: {trimmed_formula}')

def sample_range(int_data_list):
    sample_range = abs(int_data_list[0] - int_data_list[-1])
    print(f'Range: {sample_range}')

def sample_variance(given_data):
    pass

def sample_standard_deviation(given_data):
    pass
   

data_list = []
int_data_list = []

choice = int(input("1or2: "))
if choice == 1:
    while True:
        given_data = input("num: ")
        if given_data != "":
            data_list.append(given_data)
        else:
            break
    for item in data_list:
        int_data_list.append(int(item))
    int_data_list.sort()
    n_terms = len(int_data_list)
    trimmed_input = float(input("Input trim: "))
    sample_mean(int_data_list, n_terms)
    sample_median(int_data_list)
    sample_range(int_data_list)
    trimmed_mean(trimmed_input, int_data_list, n_terms)
    
