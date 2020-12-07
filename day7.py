import collections

def parseInput(fileName):
    rules = {}
    reverseRules = collections.defaultdict(set)
    with open(fileName) as f:
        for line in f:
            bagColor = line.split(" contain ")[0].split(" bag")[0]
            innerBags = line.split(" contain ")[1].replace(".", "").replace("/n", "").split(", ")
            bagDict = {}
            for bag in innerBags:
                if (bag.split(" ")[0] == "no"):
                    continue
                number = int(bag.split(" ")[0])
                color = bag.split(" ", 1)[1].split(" bag")[0]
                bagDict[color] = number
                reverseRules[color].add(bagColor)
            rules[bagColor] = Rule(bagColor, bagDict)

    return rules, reverseRules

class Rule:
    def __init__(self, name, bagDict):
        self.name = name
        self.bagDict = bagDict

def part1(fileName, bagColor):
    rules, reverseRules = parseInput(fileName)
    outerBags = set()
    for bag in reverseRules[bagColor]:
        outerBags = outerBags.union(recrusiveFunc(bag, reverseRules))

    print(outerBags)
    return len(outerBags)

def recrusiveFunc(bagColor, reverseRules):
    ruleColorSet = set()
    ruleColorSet.add(bagColor)
    if not bagColor in reverseRules:
        return ruleColorSet
    else:
        for color in reverseRules[bagColor]:
            ruleColorSet = ruleColorSet .union(recrusiveFunc(color, reverseRules))

        return ruleColorSet

def part2(fileName, bagColor):
    rules, reverseRules = parseInput(fileName)
    innerBags = 0
    print(rules[bagColor].bagDict)
    for bag,num in rules[bagColor].bagDict.items():
        innerBags = innerBags + num * recrusiveFuncPart2(bag, rules)

    print(innerBags)
    return innerBags

def recrusiveFuncPart2(ruleColor, rules):
    innerBags = 1
    if not ruleColor in rules or len(rules[ruleColor].bagDict) == 0:
        print(ruleColor)
        return 1
    else:
        rule = rules[ruleColor]
        for bag,num in rule.bagDict.items():
            innerBags = innerBags + num * recrusiveFuncPart2(bag, rules)

        return innerBags


print(part2("inputDay7", "shiny gold"))