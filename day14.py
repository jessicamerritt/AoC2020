import re

def parseInput(fileName):
    rows = []
    with open(fileName) as f:
        for line in f:
            l = line.replace("\n", "")
            rows.append(l)

    return rows

def problem1(fileName):
    instructions = parseInput(fileName)
    mask = "x"
    memMap = {}
    for inst in instructions:
        if inst.startswith("mask ="):
            mask = inst.split(" ")[2]
        else:
            mem = re.search("mem\[(\d*)\] = (\d*)", inst).group(1)
            num = int(re.search("mem\[(\d*)\] = (\d*)", inst).group(2))
            memMap[mem] = maskNum(num, mask)
    return sum(memMap.values())

def maskNum(num, mask):
    numcp = num
    numcp |= int(mask.replace('X', '0'), 2) #make all 1s 1
    numcp &= int(mask.replace('X', '1'), 2) # make all 0s 0
    return numcp


def problem2(fileName):
    instructions = parseInput(fileName)
    mask = "x"
    memMap = {}
    for inst in instructions:
        if inst.startswith("mask ="):
            mask = inst.split(" ")[2]
        else:
            mem = int(re.search("mem\[(\d*)\] = (\d*)", inst).group(1))
            num = int(re.search("mem\[(\d*)\] = (\d*)", inst).group(2))
            for m in allPossMems(mem, mask):
                memMap[m] = num
    return sum(memMap.values())


def allPossMems(mem, mask):
    mem |= int(mask.replace('X', '0'), 2) #make all 1s 1
    return recursiveFunc(mem, mask, 0)

def recursiveFunc(mem, mask, index):
    posmems = []
    for i in range(index, 36):
        char = mask[i]
        if char == "X":
            newMask0 = "0".rjust(i+1, "1").ljust(36, '1')
            newMask1 = "1".rjust(i+1, "0").ljust(36, '0')
            mem0 = mem & int(newMask0, 2)
            mem1 = mem | int(newMask1, 2)
            posmems.extend(recursiveFunc(mem0, mask, i + 1) + recursiveFunc(mem1, mask, i + 1))
            return posmems
    posmems.append(mem)
    return posmems


print(problem2("input"))

