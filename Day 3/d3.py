def partOne(stepHorizontal=3, stepVertical=1, startx=0, starty=0):
    with open("input.txt", "r") as inputFile:
        info=[]
        for line in inputFile:
            info.append(line.strip())
        x=startx + stepHorizontal
        y=starty + stepVertical
        trees=0
        while y<len(info):
            x=x%len(info[0])
            if info[y][x] == '#':
                trees+=1
            y+=stepVertical
            x+=stepHorizontal
        return trees


def partTwo():
    return partOne(1, 1)*partOne(3, 1)*partOne(5, 1)*partOne(7,1)*partOne(1, 2)


print("Answer for part one: ")
print(partOne())
print("Answer for part two: ")
print(partTwo())
