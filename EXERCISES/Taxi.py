
def taxiCompute(timeTrav, distance):
    baseFare = 40
    totalFare = baseFare + (timeTrav * 2 + distance * 13.50)
    print(f'Your total fare for the ride is {"\u20B1"}{totalFare}.')

Pass = 1
while Pass != 0:
    distance = float(input("Please input the Distance in km: "))
    timeTrav = float(input("Please input the Time in minutes: "))

    if distance and timeTrav > 0:
        taxiCompute(timeTrav, distance)
        Pass = 0
    else:
        print("Error... Please input a Non-negative number.")
        Pass = 1

# references:
# chatgpt
# 