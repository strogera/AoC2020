from collections import defaultdict

class ListNode:
    def __init__(self, value):
        self.next = None
        self.value = value

def partOneAns(node):
    x = []
    nodeOfOne = node
    node = node.next
    while node.value != nodeOfOne.value:
        x.append(str(node.value))
        node = node.next
    print(''.join(x))
    
def partOne(steps = 100, part2 = False):
    with open("input.txt", "r") as inputFile:
        cups = [int(x) for line in inputFile for x in line.strip()]
        if part2:
            cups += [x for x in range(max(cups) + 1, 1000000 + 1)]
        nodeIndex = defaultdict(ListNode)
        startingCup = ListNode(cups.pop(0))
        startingCup.next = startingCup
        nodeIndex[startingCup.value] = startingCup
        currentCup = startingCup
        for c in cups:
            newCup = ListNode(c)
            tmp = currentCup
            currentCup.next = newCup
            currentCup = newCup
            newCup.next = startingCup
            nodeIndex[c] = newCup
        
        currentCup = startingCup
        maxCupValue = max(cups)
        for count in range(steps):
            destValue = currentCup.value
            while True: 
                destValue = destValue - 1
                if destValue <= 0:
                    destValue = maxCupValue + 1
                    continue
                searchCup = currentCup
                found = False
                for _ in range(3):
                    searchCup = searchCup.next
                    if searchCup.value == destValue:
                        found = True
                        break
                if not found:
                    break
            destCup = nodeIndex[destValue]
            tmp = destCup.next
            destCup.next = currentCup.next
            for _ in range(3):
                destCup = destCup.next
            currentCup.next = destCup.next
            destCup.next = tmp

            currentCup = currentCup.next

        if part2:
            findOne = startingCup
            while True:
                if findOne.value == 1:
                    return findOne.next.value * findOne.next.next.value
                else:
                    findOne = findOne.next
        else:
            return partOneAns(nodeIndex[1])


print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partOne(10000000, True))
