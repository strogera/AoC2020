class Ship:
    direction = 1
    position = complex(0, 0)
    waypointPosition = complex(0, 0)
    moveOperation = {'E': 1, 'N':1j, 'W':-1, 'S':-1j}
    rotationOperation = {'L': 1j, 'R': -1j}

    def __init__(self, direction, shipxaxis=0, shipyaxis=0, waypointxaxis=0, waypointyaxis=0):
        self.direction = self.moveOperation[direction]
        self.poisition = complex(shipxaxis, shipyaxis)
        self.waypointPosition = complex(waypointxaxis, waypointyaxis)

    def moveShipPart1(self, instruction, value):
        #rotate the ship
        self.direction *= self.rotationOperation.get(instruction, 1) ** (value//90)
        #move the ship
        if instruction == 'F':
            self.position += self.direction * value
        else:
            self.position += self.moveOperation.get(instruction, 0) * value

    def moveShipPart2(self, instruction, value):
        #rotate the waypoint
        self.waypointPosition *= self.rotationOperation.get(instruction, 1) ** (value//90)
        if instruction == 'F':
            #move the ship
            self.position += self.waypointPosition * value
        else:
            #move the waypoint
            self.waypointPosition += self.moveOperation.get(instruction, 0) * value

    def getManhDistanceOfxyCoords(self):
        return int(abs(self.position.real) + abs(self.position.imag))

def partOne():
    with open("input.txt", "r") as inputFile:
        ship=Ship('E')
        for line in inputFile:
            ship.moveShipPart1(line[0], int(line[1:]))
        return ship.getManhDistanceOfxyCoords()

def partTwo():
    with open("input.txt", "r") as inputFile:
        ship=Ship('E', 0, 0, 10, 1)
        for line in inputFile:
            ship.moveShipPart2(line[0], int(line[1:]))
        return ship.getManhDistanceOfxyCoords()

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
