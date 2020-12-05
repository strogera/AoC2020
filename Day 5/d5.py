import math

def splitBinary(start, end, splitType):
    if splitType == 'F' or splitType == 'L':
        end-=math.ceil((end-start)/2)
    elif splitType == 'B' or splitType == 'R':
        start+=math.ceil((end-start)/2)
    return (start, end)

def partOne():
    with open("input.txt", "r") as inputFile:
        seatIds=[]
        for line in inputFile:
            line=line.strip()
            rowsStart=0
            rowsEnd=127
            for splitType in line[:-3]:
                (rowsStart, rowsEnd)=splitBinary(rowsStart, rowsEnd, splitType)
            columnsStart=0
            columnsEnd=7
            for splitType in line[-3:]:
                columnsStart, columnsEnd=splitBinary(columnsStart, columnsEnd, splitType)
            seatIds.append(rowsStart*8+columnsStart)
        return max(seatIds)


def partTwo():
    with open("input.txt", "r") as inputFile:
        seatIds=[]
        for line in inputFile:
            line=line.strip()
            rowsStart=0
            rowsEnd=127
            for splitType in line[:-3]:
                (rowsStart, rowsEnd)=splitBinary(rowsStart, rowsEnd, splitType)
            columnsStart=0
            columnsEnd=7
            for splitType in line[-3:]:
                columnsStart, columnsEnd=splitBinary(columnsStart, columnsEnd, splitType)
            seatIds.append(rowsStart*8+columnsStart)
        return set(range(min(seatIds), max(seatIds)+1)).difference(seatIds).pop()


print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
