def isEmptySeat(seat):
    return seat == '.'

def getAdjSeatsInAllDirections(grid, x, y, windowSize=-1):
    #windowSize=-1 means max
    xmax=len(grid)
    ymax=len(grid[0])
    xmin=-1
    ymin=-1
    if windowSize != -1:
        xmax=x + windowSize + 1 if windowSize + x < len(grid) else xmax
        ymax=y + windowSize + 1 if windowSize + y < len(grid[0]) else ymax
        xmin=x - windowSize - 1 if x - windowSize > 0 else xmin
        ymin=y - windowSize - 1 if y - windowSize > 0 else ymin

    adj=[]

    #North
    for xi in range(x-1, xmin, -1):
        if not isEmptySeat(grid[xi][y]):
            adj.append(grid[xi][y])
            break
    #South
    for xi in range(x+1, xmax):
        if not isEmptySeat(grid[xi][y]):
            adj.append(grid[xi][y])
            break
    #West
    for yi in range(y-1, ymin, -1):
        if not isEmptySeat(grid[x][yi]):
            adj.append(grid[x][yi])
            break
    #East
    for yi in range(y+1, ymax):
        if not isEmptySeat(grid[x][yi]):
            adj.append(grid[x][yi])
            break
    #South East
    for xi in range(x+1, xmax):
        inc=xi-x
        yi=y+inc
        if yi >= ymax:
            continue
        if not isEmptySeat(grid[xi][yi]):
            adj.append(grid[xi][yi])
            break
    #North West
    for xi in range(x-1, xmin, -1):
        inc=x-xi
        yi=y-inc
        if yi <= ymin:
            continue
        if not isEmptySeat(grid[xi][yi]):
            adj.append(grid[xi][yi])
            break
    #North East
    for xi in range(x+1, xmax):
        inc=xi-x
        yi=y-inc
        if yi <= ymin:
            continue
        if not isEmptySeat(grid[xi][yi]):
            adj.append(grid[xi][yi])
            break
    #South West
    for xi in range(x-1, xmin, -1):
        inc=x-xi
        yi=y+inc
        if yi >= ymax:
            continue
        if not isEmptySeat(grid[xi][yi]):
            adj.append(grid[xi][yi])
            break
    return adj

def countOccupied(seats):
    return seats.count('#')

def applyChanges(grid, changes):
    for (x , y) in changes.keys():
        grid[x][y]=changes[(x, y)]
    return grid

def simulate(grid, numOfAdjOccupiedToEmpty=4, adjDistance=1):
    changes={}
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            occupiedAdj=countOccupied(getAdjSeatsInAllDirections(grid, x, y, adjDistance))
            if grid[x][y] == 'L':
                if occupiedAdj == 0:
                    changes[(x, y)]='#'
            elif grid[x][y] == '#':
                if occupiedAdj >= numOfAdjOccupiedToEmpty:
                    changes[(x, y)]='L'
    grid=applyChanges(grid, changes)
    return changes != {}

def printGrid(grid):
    for x in grid:
        print(''.join(x))
    print()

def partOne():
    with open("input.txt", "r") as inputFile:
        grid=[list(x.strip()) for x in inputFile.readlines()]
        while simulate(grid): 
            pass
        return countOccupied([elem for x in grid for elem in x])

def partTwo():
    with open("input.txt", "r") as inputFile:
        grid=[list(x.strip()) for x in inputFile.readlines()]
        while simulate(grid, 5, -1): 
            pass
        return countOccupied([elem for x in grid for elem in x])

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
