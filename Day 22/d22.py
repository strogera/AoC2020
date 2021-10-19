from collections import deque

def partOne():
    with open("input.txt", "r") as inputFile:
        deck1 = deque()
        deck2 = deque()
        curDeck = 0
        for line in inputFile:
            if line == "" or line == "\n":
                continue
            if "Player" in line:
                curDeck +=1
                continue
            card=int(line.strip())
            if curDeck == 1:
                deck1.append(card)
            else:
                deck2.append(card)

        while len(deck1) != 0 and len(deck2) != 0:
            c1 = deck1.popleft()
            c2 = deck2.popleft()
            if c1 > c2:
                deck1.append(c1)
                deck1.append(c2)
            elif c2 > c1:
                deck2.append(c2)
                deck2.append(c1)
            else:
                assert(False)

        winningDeck = deck1 if len(deck1) != 0 else deck2
        return sum([winningDeck[-i-1]*(i+1) for i in range(len(winningDeck))])

def round(deck1, deck2):
    c1 = deck1.popleft()
    c2 = deck2.popleft()

    if c1 <= len(deck1) and c2 <= len(deck2):
        num = game(deque(list(deck1.copy())[:c1]), deque(list(deck2.copy())[:c2]))[1]
        if num == 1:
            deck1.append(c1)
            deck1.append(c2)
        elif num == 2:
            deck2.append(c2)
            deck2.append(c1)
        else:
            asset(False)
    else:
        if c1 > c2:
            deck1.append(c1)
            deck1.append(c2)
        elif c2 > c1:
            deck2.append(c2)
            deck2.append(c1)
        else:
            assert(False)

    return deck1, deck2

def game(deck1, deck2):
    states = []
    while len(deck1) != 0 and len(deck2) != 0 and (deck1, deck2) not in states:
        maxDeck1 = max(deck1)
        if maxDeck1 > max(deck2) and maxDeck1 > len(deck1) + len(deck2):
            return ([], 1)
        states.append((deck1.copy(), deck2.copy()))
        deck1, deck2 = round(deck1, deck2)
    return (deck2, 2) if len(deck1) == 0 else (deck1, 1)


def partTwo():
    with open("input.txt", "r") as inputFile:
        deck1 = deque()
        deck2 = deque()
        curDeck = 0
        for line in inputFile:
            if line == "" or line == "\n":
                continue
            if "Player" in line:
                curDeck +=1
                continue
            card=int(line.strip())
            if curDeck == 1:
                deck1.append(card)
            else:
                deck2.append(card)
        winningDeck = game(deck1, deck2)[0]
        return sum([winningDeck[-i-1]*(i+1) for i in range(len(winningDeck))])


print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
