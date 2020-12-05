import math

def splitBinary(start, end, splitType):
    if splitType == 'F' or splitType == 'L':
        end-=math.ceil((end-start)/2)
    elif splitType == 'B' or splitType == 'R':
        start+=math.ceil((end-start)/2)
    return (start, end)

def getRow(codes):
    rowsStart=0
    rowsEnd=127
    for splitType in codes:
        (rowsStart, rowsEnd)=splitBinary(rowsStart, rowsEnd, splitType)
    return rowsStart

def getColumn(codes):
    columnsStart=0
    columnsEnd=7
    for splitType in codes:
        columnsStart, columnsEnd=splitBinary(columnsStart, columnsEnd, splitType)
    return columnsStart

def getSeatId(row, column):
    return row*8+column

def getMissingSeatId(seatIds):
    return set(range(min(seatIds), max(seatIds)+1)).difference(seatIds).pop()

def partOne():
    with open("input.txt", "r") as inputFile:
        seatIds=[]
        for line in inputFile:
            line=line.strip()
            row=getRow(line[:-3])
            column=getColumn(line[-3:])
            seatIds.append(getSeatId(row, column))
        return max(seatIds)


def partTwo():
    with open("input.txt", "r") as inputFile:
        seatIds=[]
        for line in inputFile:
            line=line.strip()
            row=getRow(line[:-3])
            column=getColumn(line[-3:])
            seatIds.append(getSeatId(row, column))
        return getMissingSeatId(seatIds)


print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
