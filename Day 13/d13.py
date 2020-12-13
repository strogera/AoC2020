def partOne():
    with open("input.txt", "r") as inputFile:
        data=inputFile.readlines()
        earliestDeparture=int(data[0])
        buses=[int(x) for x in data[1].strip().split(',') if x != 'x']
        minTime=-1
        busId=0
        for cbus in buses:
            departureTimes=[x for x in range(earliestDeparture, earliestDeparture + max(buses)+1) if x%cbus == 0]
            for depTime in departureTimes:
                if depTime <= minTime or minTime == -1:
                    minTime = depTime
                    busId = cbus
        return busId*(minTime-earliestDeparture)



def partTwo():
    #sieving method
    #https://en.wikipedia.org/wiki/Chinese_remainder_theorem#Search_by_sieving

    with open("input.txt", "r") as inputFile:
        data=inputFile.readlines()
        buses=[int(x) if x != 'x' else -1 for x in data[1].strip().split(',') ]
        inc=[i for i in range(len(buses))]
        num=0
        accumulator=1
        for i in range(len(buses)):
            bus=buses[i]
            if bus == -1:
                continue
            increment=inc[i]
            while (num+increment) % bus != 0:
                num += accumulator
            accumulator *= bus
        return num


print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())