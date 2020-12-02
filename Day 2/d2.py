def partOne():
    with open("input.txt", "r") as inputFile:
        correctPasses=0
        for line in inputFile:
            passInfo=line.replace('-', ' ').replace(':', ' ').split()
            count=0
            for c in passInfo[3]:
                if c == passInfo[2]:
                    count+=1
            if count in range(int(passInfo[0]), int(passInfo[1])+1):
                correctPasses+=1
        print(correctPasses)
                



def partTwo():
    with open("input.txt", "r") as inputFile:
        correctPasses=0
        for line in inputFile:
            passInfo=line.replace('-', ' ').replace(':', ' ').split()
            if (passInfo[3][int(passInfo[0])-1] == passInfo[2]) != (passInfo[3][int(passInfo[1])-1] == passInfo[2]):
                correctPasses+=1
        print(correctPasses)


print("Answer for part one: ")
partOne()
print("Answer for part two: ")
partTwo()
