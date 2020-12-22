
def getNeighbors(x, y, z):
    neighbors = set()
    for xi in range(x-1, x+2):
        for yi in range(y-1, y+2):
            for zi in range(z-1, z+2):
                if xi == x and yi == y and zi==z:
                    continue
                neighbors.add((xi, yi, zi))
    return neighbors


def getActiveNeighbors(neighbors, active):
    return active.intersection(neighbors)


def simulate(active):
    newActive=set()
    discovered=set()
    for (x, y, z) in active:
        neighbors=getNeighbors(x, y, z)
        activeNeighbors=getActiveNeighbors(neighbors, active)
        if len(activeNeighbors) == 2 or len(activeNeighbors) == 3:
            newActive.add((x, y, z))
        for nx, ny, nz in neighbors:
            if (nx, ny, nz) not in discovered:
                if len(getActiveNeighbors(getNeighbors(nx, ny, nz), active)) == 3:
                    newActive.add((nx, ny, nz))
                    discovered.add((nx, ny, nz))
    return newActive


def partOne(numOfSimulations):
    active = set() 
    initialState = []
    with open("input.txt", "r") as inputFile:
        for line in inputFile:
            initialState.append(line.strip())
    z=0
    for x in range(len(initialState[0])):
        for y in range(len(initialState)):
            if initialState[x][y] == '#':
                active.add((x, y, z))

    for _ in range(numOfSimulations):
        active = simulate(active)
    return len(active)


def getNeighbors4d(x, y, z, w):
    neighbors = set()
    for xi in range(x-1, x+2):
        for yi in range(y-1, y+2):
            for zi in range(z-1, z+2):
                for wi in range(w-1, w+2):
                    if xi == x and yi == y and zi == z and wi == w:
                        continue
                    neighbors.add((xi, yi, zi, wi))
    return neighbors


def simulate4d(active):
    newActive=set()
    discovered=set()
    for (x, y, z, w) in active:
        neighbors=getNeighbors4d(x, y, z, w)
        activeNeighbors= getActiveNeighbors(neighbors, active)
        if len(activeNeighbors) == 2 or len(activeNeighbors) == 3:
            newActive.add((x, y, z, w))
        for nx, ny, nz, nw in neighbors:
            if (nx, ny, nz, nw) not in discovered:
                if len(getActiveNeighbors(getNeighbors4d(nx, ny, nz, nw), active)) == 3:
                    newActive.add((nx, ny, nz, nw))
                    discovered.add((nx, ny, nz, nw))
    return newActive


def partTwo(numOfSimulations):
    active = set() 
    initialState = []
    with open("input.txt", "r") as inputFile:
        for line in inputFile:
            initialState.append(line.strip())
    z=0
    w=0
    for x in range(len(initialState[0])):
        for y in range(len(initialState)):
            if initialState[x][y] == '#':
                active.add((x, y, z, w))

    for _ in range(numOfSimulations):
        active = simulate4d(active)
    return len(active)


print("Answer for part 1: ")
print(partOne(6))
print("Answer for part 2: ")
print(partTwo(6))
