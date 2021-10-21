def findLoopSize(publicKey):
    for subject in range(2, publicKey):
        value = 1
        for loopSize in range(1, publicKey):
            value *= subject
            value %= 20201227
            if value == publicKey:
                return loopSize

def getPublicKey(subject, loopSize):
    value = 1
    for _ in range(loopSize):
        value *= subject
        value %= 20201227
    return value


def partOne():
    with open("input.txt", "r") as inputFile:
        _, doorsPublicKey = [int(line.strip()) for line in inputFile]
        cardsLoopSize = findLoopSize(doorsPublicKey)
        return getPublicKey(doorsPublicKey, cardsLoopSize)

def partTwo():
    return 'Click the button on the site :)'

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
