
def taxiCompute(timeTrav, distance):
    baseFare = 40
    totalFare = baseFare + (timeTrav * 2 + distance * 13.50)
    print(f'Your total Fare for the ride is {"\u20B1"}{totalFare}.')


distance = float(input("Please input the Distance in km: "))
timeTrav = float(input("Please input the Time in minutes: "))
taxiCompute(timeTrav, distance)

# references:
# chatgpt
# 