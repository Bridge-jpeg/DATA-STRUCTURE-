#Author: Lyndo M. Lusac
#Description: This program checks whether the value inputted by the user are valid to make a triangle using inequality triangle theorem. 
            # It also checks if the inputted values are negative and if values are valid, it checks it checks for its Triangle type and compute its area.
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
        print("Your Triangle is Equilateral Triangle")
    elif s1 == s2 or s2 == s3 or s3 == s1:
        print("Your Triangle is Isosceles Triangle")
    else:
        print("Your Triangle is Scalene Triangle")
 
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
    print (f'The Area of your triangle is {Ar}')

# The codes below executes the program and uses all the functions defined above.
s1 = int(input("Enter the first length of your triangle: "))
s2 = int(input("Enter the second length of your triangle: "))
s3 = int(input("Enter the third length of your triangle: "))
 
if checkNeg (s1, s2, s3) == True:
    if triTheo (s1, s2, s3) == True:  
        print("It can be a triangle")
        triType(s1, s2, s3)
        area (s1, s2, s3)
    else:
        print("It is not a triangle")
else:
    print("Error... Inputed sides are invalid")