def evalParserRightPrecedence(line):
    exprStack = ['']
    result = 0
    for c in line:
        if c == '(':
            exprStack.append('')
        elif c == ')':
            parenExpr = exprStack.pop()
            exprStack[-1] += (str(eval(parenExpr)))
        elif c == '+':
            exprStack[-1] = str(eval(exprStack[-1]))
            exprStack[-1] += c
        elif c == '*':
            exprStack[-1] = str(eval(exprStack[-1]))
            exprStack[-1] += c
        elif c == '\n':
            result += eval(exprStack.pop())
        else:
            exprStack[-1] += c
    return result

def partOne():
    with open("input.txt", "r") as inputFile:
        result = 0
        for line in inputFile:
            result += evalParserRightPrecedence(line)
        return result


def evalParserAdditionHigherPrecedence(line):
    exprStack = ['']
    for c in line:
        if c == '(':
            exprStack.append('(')
            exprStack.append('')
        elif c == ')':
            curParenElems = []
            while True:
                elem = exprStack.pop()
                if elem == '(':
                    break
                curParenElems.append(str(eval(elem)))
            parenExpr = '*'.join(curParenElems)
            exprStack[-1] += str(eval(parenExpr))
        elif c == '+':
            exprStack[-1] += c
        elif c == '*':
            exprStack[-1] = str(eval(exprStack[-1]))
            exprStack.append('')
        elif c == '\n':
            exprStack[-1] = str(eval(exprStack[-1]))
        else:
            exprStack[-1] += c

    return eval('*'.join(exprStack))

def partTwo():
    with open("input.txt", "r") as inputFile:
        result = 0
        for line in inputFile:
            result += evalParserAdditionHigherPrecedence(line)
        return result

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
