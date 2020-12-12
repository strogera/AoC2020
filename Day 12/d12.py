import math

class Ship:
    xaxis=0
    yaxis=0
    direction=''
    waypointxaxis=0
    waypointyaxis=0

    def __init__(self, direction, shipxaxis=0, shipyaxis=0, waypointxaxis=0, waypointyaxis=0):
        self.xaxis = shipxaxis
        self.yaxis = shipyaxis
        self.direction = direction
        self.waypointxaxis = waypointxaxis
        self.waypointyaxis = waypointyaxis

    def moveShipPart1(self, instruction, value):
        if instruction == 'N':
            self.yaxis+=value
        elif instruction == 'S':
            self.yaxis-=value
        elif instruction == 'E':
            self.xaxis+=value
        elif instruction == 'W':
            self.xaxis-=value
        elif instruction == 'L':
            self.rotateShip(value, 'Left')
        elif instruction == 'R':
            self.rotateShip(value, 'Right')
        elif instruction == 'F':
            if self.direction == 'E':
                self.xaxis+=value
            elif self.direction == 'N':
                self.yaxis+=value
            elif self.direction == 'W':
                self.xaxis-=value
            elif self.direction == 'S':
                self.yaxis-=value

    def rotateShip(self, value, rdirection='Right'):
        if rdirection == 'Left':
            value *= 3
        for _ in range(math.floor(value/90)):
            if self.direction == 'E':
                self.direction = 'S'
            elif self.direction == 'S':
                self.direction = 'W'
            elif self.direction == 'W':
                self.direction = 'N'
            elif self.direction == 'N':
                self.direction = 'E'

    def moveShipPart2(self, instruction, value):
        if instruction == 'N':
            self.waypointyaxis+=value
        elif instruction == 'S':
            self.waypointyaxis-=value
        elif instruction == 'E':
            self.waypointxaxis+=value
        elif instruction == 'W':
            self.waypointxaxis-=value
        elif instruction == 'L':
            self.rotateWayPoint(value, 'Left')
        elif instruction == 'R':
            self.rotateWayPoint(value, 'Right')
        elif instruction == 'F':
                self.xaxis+=value*self.waypointxaxis
                self.yaxis+=value*self.waypointyaxis
    
    def rotateWayPoint(self, value, rdirection='Right'):
            for _ in range(math.floor(value/90)):
                if rdirection == 'Right':
                    self.waypointyaxis, self.waypointxaxis = self.waypointxaxis, self.waypointyaxis
                    self.waypointyaxis=self.waypointyaxis*(-1)
                elif rdirection == 'Left':
                    self.waypointyaxis, self.waypointxaxis = self.waypointxaxis, self.waypointyaxis
                    self.waypointxaxis=self.waypointxaxis*(-1)

    def getManhDistanceOfAxis(self):
        return abs(self.xaxis) + abs(self.yaxis)

def partOne():
    with open("input.txt", "r") as inputFile:
        ship=Ship('E')
        for line in inputFile:
            instruction=line[0]
            value=int(line[1:])
            ship.moveShipPart1(instruction, value)
        return ship.getManhDistanceOfAxis()

def partTwo():
    with open("input.txt", "r") as inputFile:
        ship=Ship('E', 0, 0, 10, 1)
        for line in inputFile:
            instruction=line[0]
            value=int(line[1:])
            ship.moveShipPart2(instruction, value)
        return ship.getManhDistanceOfAxis()

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
