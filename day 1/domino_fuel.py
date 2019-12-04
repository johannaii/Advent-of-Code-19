import math

def readFile():
    file = open("input_day_1.txt", encoding = "utf8")
    allLines = file.readlines()
    file.close()

    return allLines

def createFuel():
    massFile = readFile()

    fuelList = []
    for mass in massFile:
        mass = mass.strip("\n")
        mass = int(mass)
        mass = calculateFuel(mass)
        fuelList.append(mass)

    return sum(fuelList)

def calculateFuel(mass):
    totalFuel = 0
    while ((math.floor(mass/3))-2) > 0:
        mass = (math.floor(mass/3))-2
        totalFuel += mass
        print(mass)

    return totalFuel

def main():
    totalFuel = createFuel()
    print(totalFuel)

main()
