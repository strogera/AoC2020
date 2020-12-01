def partOne():
    with open("input.txt", "r") as inputFile:
        sumDict={}
        for line in inputFile:
            sumDict[int(line)]=2020-int(line)
        for x in sumDict:
           if sumDict[x] in sumDict:
               print(x*sumDict[x]) 
               return

def partTwo():
    with open("input.txt", "r") as inputFile:
        sumDict={}
        for line in inputFile:
            sumDict[int(line)]=2020-int(line)
        for x in sumDict:
            for y in sumDict:
                if x!=y:
                    if sumDict[x]-y in sumDict:
                        print(x*y*(sumDict[x]-y)) 
                        return

print("Answer for part one: ")
partOne()
print("Answer for part two: ")
partTwo()
