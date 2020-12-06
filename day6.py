def parseInput(fileName):
    entries = []
    with open(fileName) as file:
        entries=file.read().split("\n\n")
    return entries

def part1(fileName):
    rowAnswers = parseInput(fileName)
    yesCount = 0
    for row in rowAnswers:
        rowString = row.replace("\n", "")
        seenLetters = set()
        for r in rowString:
            seenLetters.add(r)
        yesCount += len(seenLetters)
    return yesCount

def part2(fileName):
    rowAnswers = parseInput(fileName)
    yesCount = 0
    for row in rowAnswers:
        rowAnswers = row.split("\n")
        numInRow = len(rowAnswers)
        #only need to check against first row
        for answerLetter in rowAnswers[0]:
            if len(filter(lambda answer: answerLetter in answer, rowAnswers)) == numInRow:
                yesCount += 1

    return yesCount

print(part2("inputDay6"))


