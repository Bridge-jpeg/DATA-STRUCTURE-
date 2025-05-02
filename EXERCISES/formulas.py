def sample_median(int_data_list):
    middle_median = len(int_data_list)/2
    value_of_numbers = len(int_data_list) % 2 == 0
    if value_of_numbers:
        even_middle_median = int(middle_median)
        even_median1 = int_data_list[even_middle_median - 1]
        even_median2 = int_data_list[even_middle_median]
        even_median = (even_median1 + even_median2)/2
        even_median_index = int(even_median)

        even_quartile1_list = int_data_list[0 : even_median_index - 1]      # quartile 1 (even)
        middle_even_quartile1 = int(len(even_quartile1_list)/2)
        even_quartile1_index1 = even_quartile1_list[middle_even_quartile1 - 1]
        even_quartile1_index2 = even_quartile1_list[middle_even_quartile1]
        even_quartile1 = (even_quartile1_index1 + even_quartile1_index2) / 2

        even_quartile3_list = int_data_list[even_median_index + 1:]     # quartile 3 (even)
        middle_even_quartile3 = int(len(even_quartile3_list)/2)
        even_quartile3_index1 = even_quartile3_list[middle_even_quartile3- 1]
        even_quartile3_index2 = even_quartile3_list[middle_even_quartile3]
        even_quartile3 = (even_quartile3_index1 + even_quartile3_index2) / 2
        even_IQR = even_quartile3 - even_quartile1
        print(f'Median: {even_median}')
        print(f"Quartile 1 (Q1): {even_quartile1}")
        print(f"Quartile 3 (Q3): {even_quartile3}")
        print(f'IQR: {even_IQR}')

    else: 
        odd_middle_median = int(middle_median - 0.5)
        odd_median = int_data_list[odd_middle_median]

        odd_quartile1_list = int_data_list[0 : odd_median -1]   # quartile 1 (odd)
        odd_quartile1_median = len(odd_quartile1_list)/2
        odd_quartile1_index = int(odd_quartile1_median - 0.5)
        odd_quartile1 = odd_quartile1_list[odd_quartile1_index]
        
        odd_quartile3_list = int_data_list[odd_median:]     # quartile 3 (odd)
        odd_quartile3_median = len(odd_quartile3_list)/2
        odd_quartile3_index = int(odd_quartile3_median - 0.5)
        odd_quartile3 = odd_quartile3_list[odd_quartile3_index]
        odd_IQR = odd_quartile3 - odd_quartile1
        print(f'Median: {odd_median}')
        print(f"Quartile 1 (Q1): {odd_quartile1}")
        print(f"Quartile 3 (Q3): {odd_quartile3}")
        print(f'IQR: {odd_IQR}')
def sample_mode(int_data_list):
    duplicated_number = []
    unique_number = []
    for data in int_data_list:     
        if data not in unique_number:
            unique_number.append(data)
        else:
            duplicated_number.append(data)
    print(f"Mode: {unique_number}")
def sample_mean(int_data_list, n_terms):
    sum_of_data = sum(int_data_list)
    global mean
    mean = (sum_of_data)/n_terms
    print(f'Mean: {round(mean, 4)}')
def trimmed_mean(trimmed_input, int_data_list):
    trimmed_decimal = trimmed_input/100
    formula_for_trimmed = int((trimmed_decimal)*(len(int_data_list) + 1))
    trimmed_datalist = int_data_list[formula_for_trimmed: -formula_for_trimmed]
    trimmed_n_terms = len(trimmed_datalist)
    sum_of_trimmed_data = sum(trimmed_datalist)
    trimmed_formula = (sum_of_trimmed_data)/trimmed_n_terms
    print(f'Trimmed Data list: {trimmed_datalist} \nTrimmed Mean: {trimmed_formula}')
def sample_range(int_data_list):
    sample_range = abs(int_data_list[-1] - int_data_list[0])
    print(f'Range: {sample_range}')
def sample_variance_and_standard_deviation(int_data_list, n_terms):
    variance_n_terms = n_terms - 1
    variance_sum_list = []
    for value in int_data_list:
        sum_numerator = (value - mean)**2
        variance_sum_list.append(sum_numerator)
    variance_numerator = sum(variance_sum_list)
    variance = round(variance_numerator/variance_n_terms, 4)
    standard_deviation = round((variance)**(0.5), 4)
    print(f'Sample Variance: {variance}')
    print(f'Standard Deviation: {standard_deviation}')
def stem_and_leaf(int_data_list):
    stem = [0.1, 0.2, 1.0, 1.2, 2.0, 2.2]
    leaf = []
    print()
    pass
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
    int_data_list.append(float(item))
int_data_list.sort()
n_terms = len(int_data_list)
trimmed_input = float(input("Input trim: "))
print("--------------------------")
print(f'The original data list: {int_data_list}')
sample_mean(int_data_list, n_terms)
sample_median(int_data_list)
sample_mode(int_data_list)
sample_range(int_data_list)
trimmed_mean(trimmed_input, int_data_list)
sample_variance_and_standard_deviation(int_data_list, n_terms)
