import re
from collections import defaultdict

def parseInput(fileName):
    with open(fileName) as file:
        string = file.read()
        [rules, ticket, others] = string.split("\n\n")
        rulesList = parseRules(rules)
        myticket = [int(x) for x in ticket.split("\n")[1].split(",")]
        otherTickets = map(lambda x: x.split(","), others.split("\n")[1:])
    return(rulesList, myticket, otherTickets)



def parseRules(rulesString):
    rulesList = []
    for rule in rulesString.split("\n"):
        (name, min1, max1, min2, max2) = re.match("(\w*|\w* \w*): (\d*)-(\d*) or (\d*)-(\d*)", rule).groups()
        rulesList.append([name, int(min1), int(max1), int(min2), int(max2)])
    return rulesList

def problem1(fileName):
    rulesList, myTicket, otherTickets = parseInput(fileName)
    wrongSum = 0
    badTickets = 0
    for ticket in otherTickets:
        print(ticket)
        answer, num = fitsAllRules(rulesList, ticket)
        if not answer:
            wrongSum += num
            badTickets += 1
    print(badTickets, len(otherTickets))
    return wrongSum


def fitsAllRules(rulesList, ticket):
    for num in ticket:
        fits = any(map(lambda x: satisfiesRule(x, num), rulesList))
        if not fits:
            return False, int(num)
    return (True, 0)

def satisfiesRule(rule, num): 
        [name, min1, max1, min2, max2] = rule
        return ((min1 <= int(num) <= max1) or (min2 <= int(num) <= max2))

def problem2(fileName):
    rulesList, myTicket, otherTickets = parseInput(fileName)
    validOthers = filter(lambda x: fitsAllRules(rulesList, x)[0], otherTickets)
    invalidRules = defaultdict(set)
    for ticket in validOthers:
        for col in range(len(ticket)):
            num = ticket[col]
            knownInvalidRules = invalidRules[col]
            rulesToCheck = set(range(len(rulesList))) - knownInvalidRules

            for i in rulesToCheck:
                rule = rulesList[i]
                if not(satisfiesRule(rule, num)):
                    invalidRules[col].add(i)
    validRules = defaultdict(set)
    for x, y in invalidRules.items():
        validRules[x] = set(range(len(rulesList))) - y

    myList = list(validRules.iteritems())
    myList.sort(lambda x, y: len(x[1]) - len(y[1]))
    takenRules = set()
    ruleToCol = [None] * 20
    for (x,y) in myList:
        y = y - takenRules
        if len(y) == 1:
            ruleNum = next(iter(y))
            takenRules.add(ruleNum)
            ruleToCol[x] = rulesList[ruleNum][0]
    answer = 1

    for i in range(len(ruleToCol)):
        name = ruleToCol[i]
        if name.startswith("departure"):
            answer *= myTicket[i]

    return answer




        

print(problem2("input"))

