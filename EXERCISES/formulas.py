def sample_median(int_data_list):
    middle_median = len(int_data_list)/2
    value_of_numbers = len(int_data_list) & 2 == 0 
    if value_of_numbers:
        even_middle_median = int(middle_median - 1)
        even_median1 = int_data_list[even_middle_median + 1]
        even_median2 = int_data_list[even_middle_median]
        even_median = (even_median1 + even_median2)/2
        print(f'Median: {even_median}')
    else: 
        odd_middle_median = int(middle_median - 0.5)
        odd_median_index = int(odd_middle_median)
        odd_median = int_data_list[odd_median_index]
        print(f'Median: {odd_median}')

def sample_mean(int_data_list, n_terms):
    sum_of_data = sum(int_data_list)
    global mean
    mean = (sum_of_data)/n_terms
    print(f'Mean: {mean}')

def trimmed_mean(trimmed_input, int_data_list, n_terms):
    trimmed_decimal = trimmed_input/100
    formula_for_trimmed = int((trimmed_decimal)*(len(int_data_list)))
    trimmed_datalist = int_data_list[formula_for_trimmed: -formula_for_trimmed]
    trimmed_n_terms = len(trimmed_datalist)
    sum_of_trimmed_data = sum(trimmed_datalist)
    trimmed_formula = (sum_of_trimmed_data)/trimmed_n_terms
    print(f'Trimmed Data list: {trimmed_datalist} \nTrimmed Mean: {trimmed_formula}')

def sample_range(int_data_list):
    sample_range = abs(int_data_list[0] - int_data_list[-1])
    print(f'Range: {sample_range}')

def sample_variance_and_standard_deviation(int_data_list, n_terms):
    variance_n_terms = n_terms - 1
    variance_mean = mean
    variance_sum_list = []
    for value in int_data_list:
        sum_numerator = (value - mean)**2
        variance_sum_list.append(sum_numerator)
    variance_numerator = sum(variance_sum_list)
    variance = round(variance_numerator/variance_n_terms, 4)
    standard_deviation = round((variance)**(0.5), 4)
    print(f'Sample Variance: {variance}')
    print(f'Standard Deviation: {standard_deviation}')

data_list = []
int_data_list = []
print("Input the all the given data and leave blank at the end.")
while True:
    given_data = input("Given: ")
    if given_data != "":
        data_list.append(given_data)
    else:
        break
for item in data_list:
    int_data_list.append(int(item))
int_data_list.sort()
n_terms = len(int_data_list)
trimmed_input = float(input("Input trim: "))
print(f'The original data list: {int_data_list}')
sample_mean(int_data_list, n_terms)
sample_median(int_data_list)
sample_range(int_data_list)
trimmed_mean(trimmed_input, int_data_list, n_terms)
sample_variance_and_standard_deviation(int_data_list, n_terms)
