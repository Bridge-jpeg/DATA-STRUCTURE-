# Name: Lyndo M. Lusac
# Description: This program ask the user for the Time travelled and Distance travelled during the ride and 
#              computes the Total Taxi fare.
# Date Submitted: March 31, 2025

def taxiCompute(timeTrav, distance):
    baseFare = 40
    totalFare = baseFare + (timeTrav * 2 + distance * 13.50)
    print(f'Your total fare for the ride is {"\u20B1"}{totalFare}.')

isValid = 1
while isValid != 0:
    distance = float(input("Please input the Distance in km: "))
    timeTrav = float(input("Please input the Time in minutes: "))

    if distance and timeTrav > 0:
        taxiCompute(timeTrav, distance)
        isValid = 0
    else:
        print("Error... Please input a Non-negative number.")
        isValid = 1