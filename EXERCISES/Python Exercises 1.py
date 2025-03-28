#Author: Lyndo M. Lusac
#Description: This program checks whether the value inputted by the user are valid to make a triangle using inequality triangle theorem. 
            # It also checks if the inputted values are negative and if values are valid, 
            # it checks for its Triangle type and compute its area.
#Date of submission: March 27, 2025

def triTheo (s1, s2, s3):
# Checks values inputted if it can formed a triangle using the Inequality Triangle Theorem.
# The sum of any two sides of a triangle is greater than or equal to the third side if not then the triangle does not exist.
    if (s1 + s2 > s3) and (s2 + s3 > s1) and (s1 + s3 > s2):  
        return True 
    else:
        return False
 
def triType (s1, s2, s3):
# Checks the Type of Triangle. 
    if s1 == s2 == s3:
        return "Equilateral"
    elif s1 == s2 or s2 == s3 or s3 == s1:
        return "Isosceles"
    else:
        return "Scalene"
 
def checkNeg (s1, s2, s3):
# Checks if the lengths inputed are negative.
    if s1 >= 0 and s2 >= 0 and s3 >= 0:
        return True
    else:
        return False

def area (s1, s2, s3): 
# Computes the area of the triangle and prints the outcome.
    s = (s1+s2+s3)/2
    Ar = (s*((s-s1)*(s-s2)*(s-s3))) ** (1/2)
    return (f'The Area of your Triangle is {round(Ar, 2)}')

# The codes below executes the program and uses all the functions defined above.
s1 = int(input("Enter the first length of your triangle: "))
s2 = int(input("Enter the second length of your triangle: "))
s3 = int(input("Enter the third length of your triangle: "))
 
if checkNeg (s1, s2, s3) == True:
    if triTheo (s1, s2, s3) == True:  
        print(f"The values inputted can be a {triType (s1, s2, s3)} Triangle and {area(s1, s2, s3)}.")
    else:
        print("Error... The values inputted cannot form a Triangle.")
else:
    print("Error... Inputted sides are invalid")