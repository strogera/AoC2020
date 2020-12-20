def parseRule(line):
   line=line.replace('or', ',')
   line=line.split(',')
   rules=[]
   for rang in line:
       rules.append(tuple(int(x) for x in rang.split('-')))   
   return rules

def parseTicket(line):
    return [int(x) for x in line.split(',')]

def isValidTicket(ticket, rules):
    valid = False
    for rule in rules.values():
        for r in rule:
            if ticket in range(r[0], r[1]+1):
                valid = True
                break
    return valid

def partOne():
    with open("input.txt", "r") as inputFile:
        rules={}
        ticket=[]
        nearbyTickets=[]
        mode='rules'
        for line in inputFile:
            if line == '\n':
                if mode == 'rules':
                    mode = 'ticket'
                elif mode == 'ticket':
                    mode = 'nearbyTicket'
                continue
            if mode == 'rules':
                ruleTemp=line.strip().split(':') 
                ruleTempParsed = parseRule(ruleTemp[1])
                rules[ruleTemp[0]] = ruleTempParsed
            elif mode == 'ticket':
                if not line.lower().startswith('your'):
                    ticket += (parseTicket(line.strip()))
            elif mode == 'nearbyTicket':
                if not line.lower().startswith('near'):
                    nearbyTickets += (parseTicket(line.strip()))
        
        summ = 0
        for nticket in nearbyTickets:
            if not isValidTicket(nticket, rules):
                summ += nticket
        return summ


def findCandidateFields(rules, tickets):
    candidateRules = []
    rejected = []
    for i in range(len(tickets[0])):
        candidateRules.append(set())
        rejected.append(set())

    for i in range(len(tickets)):
        for j in range(len(tickets[0])):
            if not isValidTicket(tickets[i][j], rules):
                continue 
            for rule in rules.keys():
                candidate=False
                for ruleOfType in rules[rule]:
                    if tickets[i][j] in range(ruleOfType[0], ruleOfType[1] + 1):
                        candidate=True
                        break
                if not candidate:
                    rejected[j].add(rule)
                    if rule in candidateRules[j]:
                        candidateRules[j].remove(rule)
                else:
                    if rule not in rejected[j]:
                        candidateRules[j].add(rule)

    for x in range(len(candidateRules)):
        candidateRules[x] = list(candidateRules[x])
    return candidateRules

def removeAlreadyFoundFields(candidateRules):
    i = 0
    while(i < len(candidateRules)):
        if len(candidateRules[i]) == 1:
            removed = False
            for j in range(0, len(candidateRules)):
                if  j != i and candidateRules[i][0] in candidateRules[j]:
                    candidateRules[j].remove(candidateRules[i][0])
                    removed = True
            if removed:
                i=0
                continue
        i += 1
    return candidateRules

def findFields(rules, tickets):
    candidateFields = findCandidateFields(rules, tickets)
    fields = removeAlreadyFoundFields(candidateFields)
    return fields



def partTwo():
    with open("input.txt", "r") as inputFile:
        rules={}
        ticket=[]
        nearbyTickets=[]
        mode='rules'
        for line in inputFile:
            if line == '\n':
                if mode == 'rules':
                    mode = 'ticket'
                elif mode == 'ticket':
                    mode = 'nearbyTicket'
                continue
            if mode == 'rules':                   
                ruleTemp=line.strip().split(':') 
                ruleTempParsed = parseRule(ruleTemp[1])
                rules[ruleTemp[0]] = ruleTempParsed

            elif mode == 'ticket':
                if not line.lower().startswith('your'):
                    ticket = parseTicket(line.strip())

            elif mode == 'nearbyTicket':
                if not line.lower().startswith('near'):
                    nearbyTickets.append(parseTicket(line.strip()))
        
        fields = findFields(rules, nearbyTickets)
        mul = 1
        for i in range(len(fields)):
            if 'departure' in fields[i][0]:
                mul *= ticket[i]
        return mul


print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
