def partOne():
    with open("input.txt", "r") as inputFile:
        direction = {"e": 2,
                    "nw":-1+1j,
                    "w":-2,
                    "se":1-1j,
                    "sw":-1-1j,
                    "ne":1+1j}
        blacked = set()
        for line in inputFile:
            point = 0 + 0j
            elems = line.strip()
            cur = ""
            for d in elems:
                if d not in direction:
                    cur = d
                    continue
                else:
                    cur += d
                point += direction[cur]
                cur = ""
            if point in blacked:
                blacked.remove(point)
            else:
                blacked.add(point)
        return len(blacked)



def partTwo():
    with open("input.txt", "r") as inputFile:
        direction = {"e": 2,
                    "nw":-1+1j,
                    "w":-2,
                    "se":1-1j,
                    "sw":-1-1j,
                    "ne":1+1j}
        blacked = set()
        for line in inputFile:
            point = 0 + 0j
            elems = line.strip()
            cur = ""
            for d in elems:
                if d not in direction:
                    cur = d
                    continue
                else:
                    cur += d
                point += direction[cur]
                cur = ""
            if point in blacked:
                blacked.remove(point)
            else:
                blacked.add(point)

        for day in range(100):
            maxx = max([int(abs(x.real)) for x in blacked]) + 3
            maxy = max([int(abs(x.imag)) for x in blacked]) + 3
            nextDayBlacked = set()
            for r in range(-maxx, maxx+1):
                for im in range(-maxy, maxy+1):
                    point = complex(r, im)
                    countBlackAdj = 0
                    for adj in direction.values():
                        if point+adj in blacked:
                            countBlackAdj += 1
                    if point in blacked:
                        if countBlackAdj <= 2 and countBlackAdj != 0:
                            nextDayBlacked.add(point)
                    else:
                        if countBlackAdj == 2:
                            nextDayBlacked.add(point)
            blacked = nextDayBlacked
        return len(blacked)



print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
