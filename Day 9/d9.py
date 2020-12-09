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
    for i in range(len(l)):
        summ=l[i]
        nums=[l[i]]
        for j in range(i+1, len(l)):
            summ+=l[j]
            nums.append(l[j])
            if summ == num:
                return nums
            elif summ > num:
                break

def partTwo(num=88311122):
    with open("input.txt", "r") as inputFile:
        data=[int (x) for x in inputFile.readlines()]
        subSet=getSubsetSumsTo(data, num)
        return max(subSet)+min(subSet)

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
