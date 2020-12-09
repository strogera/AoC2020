def getNumNoSumPair(data, preamble):
    queue=data[:preamble]

    for x in data[preamble:]:
        for q in queue:
            sumExists=False

            if x-q in queue:
                sumExists=True
                break

        if not sumExists:
            return x

        queue.pop(0)
        queue.append(x)

def partOne(preamble=25):
    with open("input.txt", "r") as inputFile:
        data=[int (x) for x in inputFile.readlines()]
        return getNumNoSumPair(data, preamble)

def getSubsetSumsTo(l, num):
    numsQueue=[]
    summ=0
    for x in l:
        summ+=x
        numsQueue.append(x)

        while summ > num and len(numsQueue) > 2:
            n=numsQueue.pop(0)
            summ-=n

        if summ == num:
            return numsQueue
        

def partTwo(num):
    with open("input.txt", "r") as inputFile:
        data=[int (x) for x in inputFile.readlines()]
        subSet=getSubsetSumsTo(data, num)
        subSet=sorted(subSet)
        return subSet[0]+subSet[-1]

partOneAnswer=partOne()
print("Answer for part 1: ")
print(partOneAnswer)
print("Answer for part 2: ")
print(partTwo(partOneAnswer))
