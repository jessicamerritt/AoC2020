import re

def parseInput(fileName):
    entries = []
    with open(fileName) as file:
        entries=file.read().split("\n\n")
    return entries

def isLineValidPart1(entryKeys):
    necessaryFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    necessaryFieldsPlusOptional = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    if(len(entryKeys) < len(necessaryFields)):
        return False

    return all(e in entryKeys for e in necessaryFields)


def isLineValid(entryMap):
    entryKeys = entryMap.keys()
    if (not isLineValidPart1(entryKeys)):
        return False

    eclOptions = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    byr = int(entryMap.get("byr"))
    byrValid = byr >= 1920 and byr <= 2002
    iyr = int(entryMap.get("iyr"))
    iyrValid = iyr >= 2010 and iyr <= 2020
    eyr = int(entryMap.get("eyr"))
    eyrValid = eyr >= 2020 and eyr <= 2030
    hgt = entryMap.get("hgt")
    hgtValid = (hgt[-2:] == "cm" and (int(hgt[:-2]) >= 150 and int(hgt[:-2]) <= 193)) or (hgt[-2:] == "in" and (int(hgt[:-2]) >= 59 and int(hgt[:-2]) <= 76))
    hcl = entryMap.get("hcl")
    hclValid = re.search("#[0-9a-f]{6}", hcl) != None
    ecl = entryMap.get("ecl")
    eclValid = ecl in eclOptions
    pid = entryMap.get("pid")
    pidValid = len(pid) == 9
    #print(byrValid , iyrValid , eyrValid , hgtValid , hclValid , hclValid , eclValid , pidValid)

    return byrValid and iyrValid and eyrValid and hgtValid and hclValid and hclValid and eclValid and pidValid


def problem1(fileName):
    entries = parseInput(fileName)
    totalValid = 0

    for e in entries:
        line = e.replace('\n', ' ')
        fieldAndValue = {x.split(":")[0]:x.split(":")[1] for x in line.split(" ")}
        if (isLineValidPart1(fieldAndValue.keys())):
            totalValid+=1

    return totalValid

def problem2(fileName):
    entries = parseInput(fileName)
    totalValid = 0

    for e in entries:
        line = e.replace('\n', ' ')
        fieldAndValue = {x.split(":")[0]:x.split(":")[1] for x in line.split(" ")}
        if (isLineValid(fieldAndValue)):
            totalValid+=1


    print(totalValid)
    return totalValid

print(problem2("inputDay4"))