def parseInput(fileName):
    rows = []
    with open(fileName) as f:
        for line in f:
            rows.append(line)

    return rows

def problem1(fileName, right, down):
    tree = "#"
    safe = "."
    treeMap = parseInput(fileName)
    slope = 3
    totalTreeCount = 0
    pos = 0
    rowNum = 0
    for row in treeMap:
        if (rowNum % down == 0):
            onTree = row[pos] == tree
            if (onTree):
                totalTreeCount+=1
            pos = (pos + right) % 31
            print(rowNum)
        rowNum+=1
        

    print(totalTreeCount)
    return totalTreeCount


print(problem1("DayThreeInput", 1, 1) * problem1("DayThreeInput", 3, 1) * problem1("DayThreeInput", 5, 1) * problem1("DayThreeInput", 7, 1) * problem1("DayThreeInput", 1, 2))