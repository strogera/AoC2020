from collections import defaultdict
from itertools import product

def removeValueFromDictExceptForKey(dictionary, value, key):
    for k in dictionary:
        if value in dictionary[k]:
            if key != k:
                dictionary[k].remove(value)
    return dictionary

def partOne(part2 = False):
    with open("input.txt", "r") as inputFile:
        possibleAllergToFood  = defaultdict(set)
        foodListInput =  []
        for line in inputFile:
            elems=line.strip().replace(')', '').replace(',', '').split('(')
            allergens = set(elems[1].replace('contains','').split())
            food =  set(elems[0].split())
            for a in allergens:
                possibleAllergToFood[a] |= food
            foodListInput.append((food, allergens))

        for (l1, l2) in product(foodListInput, foodListInput):
            if l1 == l2:
                continue
            for al in l1[1]:
                if al in l2[1]:
                    diff = l1[0] - l2[0]
                    possibleAllergToFood[al] -= diff
                    if len(possibleAllergToFood[al]) == 1:
                        removeValueFromDictExceptForKey(possibleAllergToFood, list(possibleAllergToFood[al])[0], al)

        definiteAllergens = set([list(x)[0] for x in possibleAllergToFood.values() if len(x) == 1])
        count = 0
        for (f, al) in foodListInput:
            for incredient in f:
                if incredient not in definiteAllergens:
                    count += 1

        print("Answer for part 1: ")
        print(count)
        if part2:
            print("Answer for part 2: ")
            print(','.join([possibleAllergToFood[x].pop() for x in sorted(possibleAllergToFood)]))


partOne(True)
