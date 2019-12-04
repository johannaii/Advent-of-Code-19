import math

def readFile():
    file = open("input_day_1.txt", encoding = "utf8")
    allLines = file.readlines()
    file.close()

    return allLines

def calculateFuel():
    massFile = readFile()

    fuelList = []
    for mass in massFile:
        mass = mass.strip("\n")
        mass = int(mass)
        mass = (math.floor(mass/3))-2
        print(mass)
        fuelList.append(mass)


    return sum(fuelList)

def main():
    totalFuel = calculateFuel()
    print(totalFuel)

main()
