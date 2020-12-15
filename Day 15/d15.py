def partOne(iterations):
    with open("input.txt", "r") as inputFile:
        elems=[int(x) for x in inputFile.read().strip().split(',')]

        summs=[-1]*(iterations + 1)
        rev = [(-1, -1)]*(iterations + 1)

        for i, num in enumerate(elems):
            summs[i+1] = num
            rev[num] = (i + 1, i + 1)

        for i in range(len(elems)+1, iterations+1):
            prev = summs[i-1]
            if prev == -1 or rev[prev][0] == -1 or rev[prev][1] == -1 :
            #first time or once
                summs[i] = 0
                rev[0] = (rev[0][1], i)
            else:
                summs[i] = rev[prev][1] - rev[prev][0]
                rev[summs[i]] = (rev[summs[i]][1], i)            

        return summs[iterations]
                


print("Answer for part 1: ")
print(partOne(2020))
print("Answer for part 2: ")
print(partOne(30000000))