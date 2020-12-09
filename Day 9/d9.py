def getSumCouples(l):
    summs=[]
    for i in range(len(l)):
        for j in range(i, len(l)):
            summs.append(l[i]+l[j])
    return summs

def partOne(preamble=25):
    with open("input.txt", "r") as inputFile:
        data=[int (x) for x in inputFile.readlines()]
        for i in range(len(data)):
            if i < preamble:
                continue
            
            sumCouples=getSumCouples(data[i-preamble:i])
            num=data[i]

            if num not in sumCouples:
                return num

def getSubsetSumsTo(l, num):
    numsQueue=[]
    summ=0
    for x in l:
        summ+=x
        numsQueue.append(x)

        while summ > num:
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
