def partOne(iterations):
    with open("input.txt", "r") as inputFile:
        elems=[int(x) for x in inputFile.read().strip().split(',')]

        numberAtTurn=[-1]*(iterations + 1)
        previouslySeen = [(-1, -1)]*(iterations + 1)

        for i, num in enumerate(elems):
            numberAtTurn[i+1] = num
            previouslySeen[num] = (i + 1, i + 1)

        for i in range(len(elems)+1, iterations+1):
            previousNumber = numberAtTurn[i-1]
            if previousNumber == -1 or previouslySeen[previousNumber][0] == -1 or previouslySeen[previousNumber][1] == -1 :
            #first time or once
                numberAtTurn[i] = 0
                previouslySeen[0] = (previouslySeen[0][1], i)
            else:
                numberAtTurn[i] = previouslySeen[previousNumber][1] - previouslySeen[previousNumber][0]
                previouslySeen[numberAtTurn[i]] = (previouslySeen[numberAtTurn[i]][1], i)            

        return numberAtTurn[iterations]
                

def partOneAlt(iterations):
    #Alternative solution without using too much memory
    with open("input.txt", "r") as inputFile:
        nums={int(x): i+1 for i, x in enumerate(inputFile.read().strip().split(','))}
        turn=len(nums)+1
        numCurrent=0
        while(turn < iterations):
            numPrev=nums.get(numCurrent)
            nums[numCurrent] = turn
            if numPrev:
                numCurrent = turn - numPrev 
            else:
                numCurrent=0
            turn +=1
        return numCurrent


print("Answer for part 1: ")
print(partOne(2020))
#print(partOneAlt(2020))
print("Answer for part 2: ")
print(partOne(30000000))
#print(partOneAlt(30000000))