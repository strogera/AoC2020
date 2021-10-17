from math import sqrt

def orientCorner(edgeList, edgeListAll, tile, orientation):
    assert(orientation in ["NE", "SE", "NW", "SW"])
    ways = []
    outer = []
    for edge in edgeList:
        if edgeListAll.count(edge) == 1 and edgeListAll.count(edge[::-1]) == 1:
            outer.append(edge)
            outer.append(edge[::-1])

    for _ in range(2):
        for _ in range(4):
            if "N" in orientation :
                if tile[0] in outer:
                    if "W" in orientation:
                        if getWestEdge(tile) in outer: 
                            ways.append(tile)
                    elif "E" in orientation:
                        if getEastEdge(tile) in outer: 
                            ways.append(tile)
            elif "S" in orientation:
                if tile[-1] in outer:
                    if "W" in orientation:
                        if getWestEdge(tile) in outer: 
                            ways.append(tile)
                    elif "E" in orientation:
                        if  getEastEdge(tile) in outer: 
                            ways.append(tile)
            tile = rotate(tile)
        tile = flip(tile)
    assert(len(ways) != 0)
    return ways

def fitAnchorToTileOneSide(anchorTile, tileToFit, anchorSide):
    assert(anchorSide in ["N", "S", "E", "W"])
    for _ in range(2):
        for _ in range(4):
            if testSide(anchorTile, tileToFit, anchorSide):
                return tileToFit
            tileToFit = rotate(tileToFit)
        tileToFit = flip(tileToFit)

def testSide(anchorTile, tile, anchorSide):
    if anchorSide == "N":
        return anchorTile[0] == tile[-1]
    elif anchorSide == "S":
        return anchorTile[-1] == tile[0]
    elif anchorSide == "E":
        return getEastEdge(anchorTile) == getWestEdge(tile)
    elif anchorSide == "W":
        return getWestEdge(anchorTile) == getEastEdge(tile)

def fitAnchorToTileTwoSides(anchorTile1, anchorTile2, tileToFit, anchorSide1, anchorSide2):
    for _ in range(2):
        for _ in range(4):
            if testSide(anchorTile1, tileToFit, anchorSide1) and testSide(anchorTile2, tileToFit, anchorSide2):
                return tileToFit
            tileToFit = rotate(tileToFit)
        tileToFit = flip(tileToFit)


def orientEdge(edge, tile, orientation):
    for _ in range(2):
        for _ in range(4):
            if 'N' in orientation:
                if tile[0] == edge:
                    return tile
            elif 'S' in orientation:
                if tile[-1] == edge:
                    return tile
            elif 'W' in orientation:
                if getWestEdge(tile) == edge:
                    return tile
            elif 'E' in orientation:
                if getEastEdge(tile) == edge:
                    return tile
            tile = rotate(tile)
        tile = flip(tile)
    assert(False)

def rotate(image):
    return list(''.join(list(x)) for x in zip(*image))[::-1]

def flip(image):
    return list(reversed(image))

def getWestEdge(image):
    return ''.join([row[0] for row in image])

def getEastEdge(image):
    return ''.join([row[-1] for row in image])




def partOne():
    with open("input.txt", "r") as inputFile:
        images = {}
        image = []
        for line in inputFile:
            if line == '\n':
                if image != []:
                    images[tileId] = image
                image = []
                continue

            line = line.strip()
            if ':' in line:
                tileId = int(line.replace(':', '')[5:])
            else:
                image.append(line)
        if image != []:
            images[tileId] = image

        edges = {}
        edgeListAll = []
        for id in images:
            edgeList = []
            edgeList.append(images[id][0])
            edgeList.append(images[id][-1])
            edgeLeft = ''
            edgeRight = ''
            for row in images[id]:
                edgeLeft += row[0]
                edgeRight += row[-1]
            edgeList.append(edgeLeft)
            edgeList.append(edgeRight)
            edges[id] = edgeList
            edgeListAll += edgeList
            edgeList = [x[::-1] for x in edgeList if x[::-1] != x]
            edgeListAll += edgeList
        score = 1
        for id in edges:
            count = 0
            for edge in edges[id]:
                if edgeListAll.count(edge) == 1 and edgeListAll.count(edge[::-1]) == 1:
                    count += 1
            if count == 2:
                score *= id
        return score


def actualImage(image):
    newImage = []
    for rowIndex in range(len(image)):
        newImage.append([])
        for i in range(1, len(image[rowIndex][0]) - 1):
            newImage[rowIndex].append("")
            for columnIndex in range(len(image[rowIndex])):
                newImage[rowIndex][i-1] += image[rowIndex][columnIndex][i][1:-1]
    #print('\n'.join(sum(newImage, [])))
    return sum(newImage, [])


def partTwo():
    with open("input.txt", "r") as inputFile:
        images = {}
        image = []
        for line in inputFile:
            if line == '\n':
                if image != []:
                    images[tileId] = image
                image = []
                continue

            line = line.strip()
            if ':' in line:
                tileId = int(line.replace(':', '')[5:])
            else:
                image.append(line)
        if image != []:
            images[tileId] = image

        edges = {}
        edgeListAll = []
        for id in images:
            edgeList = []
            edgeList.append(images[id][0])
            edgeList.append(images[id][-1])
            edgeLeft = ''
            edgeRight = ''
            for row in images[id]:
                edgeLeft += row[0]
                edgeRight += row[-1]
            edgeList.append(edgeLeft)
            edgeList.append(edgeRight)
            edges[id] = edgeList
            edgeListAll += edgeList
            edgeList = [x[::-1] for x in edgeList if x[::-1] != x]
            edgeListAll += edgeList

        corners = set()
        edgess = set()
        inner = set()
        for id in edges:
            count = 0
            for edge in edges[id]:
                if edgeListAll.count(edge) == 1 and edgeListAll.count(edge[::-1]) == 1:
                    count += 1
            if count == 2:
                corners.add(id)
            elif count == 1:
                edgess.add(id)
            else:
                inner.add(id)
            
        newImage = []
        imageSize = int(sqrt(len(images))) 
        for x in range(imageSize):
            newImage.append([])
        for rowIndex in range(len(newImage)):
            for columnIndex in range(len(newImage)):
                if rowIndex == 0:
                    if columnIndex == 0: 
                        corner = corners.pop()
                        newImage[rowIndex].append(orientCorner(edges[corner], edgeListAll, images[corner], "NW")[0])
                    elif columnIndex == len(newImage) - 1:
                        cornToDelete = -1
                        for c in corners:
                            found = False
                            for test in orientCorner(edges[c], edgeListAll, images[c], "NE"):
                                if testSide(newImage[rowIndex][columnIndex-1], test, "E"):
                                    newImage[rowIndex].append(test)
                                    cornToDelete = c
                                    found = True
                                    break
                            if found:
                                break
                        if cornToDelete != -1:
                            corners.remove(cornToDelete)
                            break
                        else:
                            print(rowIndex, columnIndex)
                            assert(False)
                    else:
                        edgeFit = -1
                        for edge in edgess:
                            test = fitAnchorToTileOneSide(newImage[rowIndex][columnIndex-1], images[edge], "E")
                            if test:
                                newImage[rowIndex].append(test)
                                edgeFit = edge
                                break
                        if edgeFit != -1:
                            edgess.remove(edgeFit)
                        else:
                            break
                elif rowIndex == len(newImage) - 1:
                    if columnIndex == 0:
                        toDelete = -1
                        for c in corners:
                            found = False
                            for test in orientCorner(edges[c], edgeListAll, images[c], "SW"):
                                if testSide(newImage[rowIndex - 1][columnIndex], test, "S"):
                                    newImage[rowIndex].append(test)
                                    toDelete = c
                                    break
                            if found:
                                break
                        if toDelete != -1:
                            corners.remove(toDelete)
                        else:
                            assert(False)
                    elif columnIndex == len(newImage) - 1:
                        c = corners.pop()
                        for test in orientCorner(edges[c], edgeListAll, images[c], "SE"):
                            if testSide(newImage[rowIndex][columnIndex-1], test, "E"):
                                newImage[rowIndex].append(test)
                    else:
                        toDelete = -1
                        for tid in edgess:
                            test = fitAnchorToTileTwoSides(newImage[rowIndex][columnIndex-1],
                             newImage[rowIndex - 1][columnIndex],
                             images[tid], "E", "S")
                            if test:
                                newImage[rowIndex].append(test)
                                toDelete = tid
                                found = True
                                break
                        if toDelete != -1:
                            edgess.remove(tid)
                        else:
                            assert(False)
                else:
                    if columnIndex == 0:
                        edgeFit = -1
                        for edge in edgess:
                            test = fitAnchorToTileOneSide(newImage[rowIndex-1][columnIndex], images[edge], "S")
                            if test:
                                newImage[rowIndex].append(test)
                                edgeFit = edge
                                break
                        if edgeFit != -1:
                            edgess.remove(edgeFit)
                    elif columnIndex == len(newImage) - 1:
                        toDelete = -1
                        for tid in edgess:
                            test = fitAnchorToTileTwoSides(newImage[rowIndex][columnIndex-1],
                             newImage[rowIndex - 1][columnIndex],
                             images[tid], "E", "S")
                            if test:
                                newImage[rowIndex].append(test)
                                toDelete = tid 
                                break
                        if toDelete == -1:
                            assert(False)
                        edgess.remove(toDelete)
                    else:
                        toDelete = -1
                        for tid in inner:
                            test = fitAnchorToTileTwoSides(newImage[rowIndex][columnIndex-1],
                             newImage[rowIndex - 1][columnIndex],
                             images[tid], "E", "S")
                            if test:
                                newImage[rowIndex].append(test)
                                toDelete = tid
                                break
                        if toDelete != -1:
                            inner.remove(toDelete)
                        else:
                            assert(False)
        return waterRoughness(actualImage(newImage))


def waterRoughness(image):
    monster =  ['                  # ',
                '#    ##    ##    ###',
                ' #  #  #  #  #  #   ']
    monsterPositions = set()

    for _ in range(2):
        for _ in range(4):
            for x in range(len(image)):
                for y in range(len(image[x])):
                    if x + len(monster) <= (len(image)) and y+len(monster[0]) <= (len(image[x])):
                        notAmonster = False
                        
                        monCurr = set()
                        for xi in range(x, x+len(monster)):
                            for yi in range(y, y+len(monster[0])):
                                if monster[xi - x][yi-y] == '#':
                                    if image[xi][yi] == '#':
                                        monCurr.add((xi,yi))
                                    else:
                                        notAmonster = True
                                        break
                            if notAmonster:
                                monCurr = set()
                                break
                    monsterPositions |= monCurr
            monster = rotate(monster)
        monster = flip(monster)
    return ''.join(image).count('#') - len(monsterPositions)

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
