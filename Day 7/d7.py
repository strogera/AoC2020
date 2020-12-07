from collections import defaultdict

def findBagsContainingBag(bagGraph, bagToFind):
    l=[]
    for bag, _ in list(bagGraph.items()):
        if bagToFind in bagGraph[bag]:
            l.append(bag)
    return l

def findAllNestedBagsContainingBag(bagGraph, bag):
    containsBagToFind=set()
    bagsToCheck=findBagsContainingBag(bagGraph, bag)
    while(len(bagsToCheck)!=0):
        l=[]
        for cbag in bagsToCheck:
            if cbag not in containsBagToFind:
                containsBagToFind.add(cbag)
                l+=findBagsContainingBag(bagGraph, cbag)
        bagsToCheck=l
    return containsBagToFind

def countContainingBags(bagGraph, fromBag):
    bag=bagGraph[fromBag]
    if bag == []:
        return 0
    count=0
    for cbag in bag:
        n1=cbag[0]
        nextBag=cbag[1]
        n2=countContainingBags(bagGraph, nextBag)
        count+=n1 + n1 * n2
    return count

def partOne(bagToFind):
    with open("input.txt", "r") as inputFile:
        bagGraph=defaultdict(list)
        for line in inputFile:
            input=line.strip().replace('.', '').split()
            bagName=''.join(input[:2])
            bagContains=' '.join(input[4:]).split(',')
            for contained in bagContains:
                contained=contained.split()
                if contained[0] != 'no':
                    containedBagName=''.join(contained[1:-1])
                    if bagName not in bagGraph:
                        bagGraph[bagName]=[containedBagName]
                    else:
                        bagGraph[bagName].append(containedBagName)
        return len(findAllNestedBagsContainingBag(bagGraph, bagToFind))

def partTwo(rootBag):
    with open("input.txt", "r") as inputFile:
        bagGraph=defaultdict(list)
        for line in inputFile:
            input=line.strip().replace('.', '').split()
            bagName=''.join(input[:2])
            bagContains=' '.join(input[4:]).split(',')
            for contained in bagContains:
                contained=contained.split()
                if contained[0] != 'no':
                    containedBagName=''.join(contained[1:-1])
                    containedNum=int(contained[0])
                    if bagName not in bagGraph:
                        bagGraph[bagName]=[(containedNum, containedBagName)]
                    else:
                        bagGraph[bagName].append((containedNum, containedBagName))
        return countContainingBags(bagGraph, rootBag)

print("Answer for part 1: ")
print(partOne('shinygold'))
print("Answer for part 2: ")
print(partTwo('shinygold'))
