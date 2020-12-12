import math
def rotate(shipDirection, value, direction='Right'):
    if direction == 'Left':
        value *= 3
    for _ in range(math.floor(value/90)):
        if shipDirection == 'E':
            shipDirection = 'S'
        elif shipDirection == 'S':
            shipDirection = 'W'
        elif shipDirection == 'W':
            shipDirection = 'N'
        elif shipDirection == 'N':
            shipDirection = 'E'
    return shipDirection

def moveShip(xaxis, yaxis, shipDirection, instruction, value):
    if instruction == 'N':
        yaxis+=value
    elif instruction == 'S':
        yaxis-=value
    elif instruction == 'E':
        xaxis+=value
    elif instruction == 'W':
        xaxis-=value
    elif instruction == 'L':
        shipDirection=rotate(shipDirection, value, 'Left')
    elif instruction == 'R':
        shipDirection=rotate(shipDirection, value, 'Right')
    elif instruction == 'F':
        if shipDirection == 'E':
            xaxis+=value
        elif shipDirection == 'N':
            yaxis+=value
        elif shipDirection == 'W':
            xaxis-=value
        elif shipDirection == 'S':
            yaxis-=value
    return xaxis, yaxis

def partOne():
    with open("input.txt", "r") as inputFile:
        shipDirection='E'
        xaxis=0
        yaxis=0
        for line in inputFile:
            instruction=line[0]
            value=int(line[1:])
            xaxis, yaxis = moveShip(xaxis, yaxis, shipDirection,  instruction, value)
        return abs(xaxis) + abs(yaxis)


def partTwo():
    with open("input.txt", "r") as inputFile:
        shipxaxis=0
        shipyaxis=0
        waypointxaxis=10
        waypointyaxis=1
        for line in inputFile:
            instruction=line[0]
            value=int(line[1:])
            if instruction == 'N':
                waypointyaxis+=value
            elif instruction == 'S':
                waypointyaxis-=value
            elif instruction == 'E':
                waypointxaxis+=value
            elif instruction == 'W':
                waypointxaxis-=value
            elif instruction == 'L':
                for _ in range(math.floor(value/90)):
                    waypointyaxis, waypointxaxis = waypointxaxis, waypointyaxis
                    waypointxaxis=waypointxaxis*(-1)
            elif instruction == 'R':
                for _ in range(math.floor(value/90)):
                    waypointyaxis, waypointxaxis = waypointxaxis, waypointyaxis
                    waypointyaxis=waypointyaxis*(-1)
            elif instruction == 'F':
                    shipxaxis+=value*waypointxaxis
                    shipyaxis+=value*waypointyaxis
        return abs(shipxaxis) + abs(shipyaxis)

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
