def execute(program):
    accumulator=0
    programIndex=0
    instrSet=set()
    while(programIndex < len(program)):
        ins, arg=program[programIndex]
        if programIndex in instrSet:
            return accumulator
        else:
            instrSet.add(programIndex)
        if ins == 'nop':
            programIndex+=1
        elif ins == 'acc':
            accumulator+=arg
            programIndex+=1
        elif ins == 'jmp':
            programIndex+=arg

def partOne():
    with open("input.txt", "r") as inputFile:
        program=[]
        for line in inputFile:
            elems=line.strip().split()
            instruction=elems[0]
            argument=int(elems[1])
            program.append((instruction, argument))
        return execute(program)

def execute2(program, changed):
    accumulator=0
    programIndex=0
    instrSet=set()
    changeFlag=False
    while(programIndex<len(program)):
        ins, arg=program[programIndex]
        if programIndex in instrSet:
            return True
        else:
            instrSet.add(programIndex)
        if ins == 'nop':
            if programIndex not in changed and not changeFlag:
                changed.add(programIndex)
                programIndex+=arg
                changeFlag=True
            else:
                programIndex+=1
        elif ins == 'acc':
            accumulator+=arg
            programIndex+=1
        elif ins == 'jmp':
            if programIndex not in changed and not changeFlag:
                changed.add(programIndex)
                changeFlag=True
                programIndex+=1
            else:
                programIndex+=arg
    return accumulator


def partTwo():
    with open("input.txt", "r") as inputFile:
        program=[]
        for line in inputFile:
            elems=line.strip().split()
            instruction=elems[0]
            argument=int(elems[1])
            program.append((instruction, argument))
        changed=set()
        loop=True
        while(loop == True):
            loop=execute2(program, changed)
        return loop

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
