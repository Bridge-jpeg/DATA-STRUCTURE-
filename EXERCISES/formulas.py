# sample_mean = float(input("number: ")) # mean



def sample_mean(given, no_terms):
    inp_Number = []
    while True:
        inp = input("Input number: ")
        try:
            if inp == "":
                break
        except:
            digit = int(inp)
            inp_Number.append(digit)
    
    print(*inp_Number, sep = "\n")


given = int(input("numer: ")) #Xi
no_terms = int(input("terms: "))
sample_mean(given, no_terms)