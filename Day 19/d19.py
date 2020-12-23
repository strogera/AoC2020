def check(message, ruleSeq, rules):
    if message == [] or len(ruleSeq) == 0: 
        return message == [] and ruleSeq == []

    if not rules[ruleSeq[0]][0][0].isnumeric():
        if message[0] in (rules[ruleSeq[0]][0]):
            return check(message[1:], ruleSeq[1:], rules)
        else:
            return False
    else:
        matched = False
        for altRule in rules[ruleSeq[0]]:
            matched = check(message, altRule + ruleSeq[1:], rules)

            if matched == True:
                break

        return matched

    return False

def partOne():
    with open("input.txt", "r") as inputFile:
        rulesMode = True
        rules = {}
        res = []
        for line in inputFile:
            if line == '\n':
                rulesMode = False
                continue

            line=line.strip()
            if rulesMode:
                ruleNum, rulesRaw =  line.split(':')
                if '|' in rulesRaw:
                    rule1, rule2 = rulesRaw.split('|')
                    rules[ruleNum] = [rule1.split(), rule2.split()]
                else:
                    rulesRaw = rulesRaw.replace('"', '')
                    rules[ruleNum] = [rulesRaw.split()]
            else:
                res.append(check(list(line), ['0'], rules))
        return (sum(res))


def partTwo():
    with open("input.txt", "r") as inputFile:
        rulesMode = True
        rules = {}
        res = []
        for line in inputFile:
            if line == '\n':
                rulesMode = False
                #updateRules
                rules['8'] = [['42'],  [ '42', '8']]
                rules['11'] = [['42', '31'],['42', '11', '31']]
                continue

            line=line.strip()
            if rulesMode:
                ruleNum, rulesRaw =  line.split(':')
                if '|' in rulesRaw:
                    rule1, rule2 = rulesRaw.split('|')
                    rules[ruleNum] = [rule1.split(), rule2.split()]
                else:
                    rulesRaw = rulesRaw.replace('"', '')
                    rules[ruleNum] = [rulesRaw.split()]
            else:
                res.append(check(list(line), ['0'], rules))
        return (sum(res))


print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
