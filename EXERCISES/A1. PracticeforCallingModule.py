from ModulesforA1 import checkNeg, triTheo, triType, area

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