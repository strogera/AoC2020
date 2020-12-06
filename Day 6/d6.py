def partOne():
    with open("input.txt", "r") as inputFile:
        groupData=inputFile.read().strip().split('\n\n')
        allGroupsYesAns=0
        for group in groupData:
            currentGroupYesAns=set()
            for ans in group.replace('\n', ''):
                currentGroupYesAns.add(ans)
            allGroupsYesAns+=len(currentGroupYesAns)
        return allGroupsYesAns
            



def partTwo():
    with open("input.txt", "r") as inputFile:
        groupData=inputFile.read().strip().split('\n\n')
        allGroupsYesAns=0
        for group in groupData:
            group=group.split('\n')
            currentGroupYesAns={}
            for ans in group:
                for singleAns in ans:
                    if singleAns in currentGroupYesAns.keys():
                        currentGroupYesAns[singleAns]+=1
                    else:
                        currentGroupYesAns[singleAns]=1
            allGroupsYesAns+=len([x for x in currentGroupYesAns.keys() if currentGroupYesAns[x] == len(group)])
        return allGroupsYesAns 

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
