import copy

seat = "L"
floor = "."
taken = "#"
unoccupied = [seat, floor]

def parseInput(fileName):
    lines = []
    with open(fileName) as f:
        for line in f:
            l = line.replace("\n", "")
            lines.append(list(l))

    return lines

def part1(fileName):
    seatMap = parseInput(fileName)
    height = len(seatMap)
    width = len(seatMap[0])
    iterations = 0
    changes = 1
    while not changes == 0:
        seatMap, changes = calculateNextMap(seatMap)
        iterations+=1
    return sum(map(lambda l: l.count(taken), seatMap))

def calculateNextMap(seatMap):
    changes = 0
    height = len(seatMap)
    width = len(seatMap[0])
    newMap = [[i for i in row] for row in seatMap]
    for i in range(height):
        row = seatMap[i]
        for j in range(width):
            spot = row[j]
            adjacentSeats = getNeighbors(seatMap, i, j)
            print(adjacentSeats)
            if spot == seat and not taken in adjacentSeats:
                changes+=1
                newMap[i][j] = taken
            elif spot == taken and adjacentSeats.count(taken) >= 4:
                changes+=1
                newMap[i][j] = seat
    return (newMap, changes)

def getNeighbors(seatMap, rownum, spotNum):
    lastRow = len(seatMap) - 1
    lastCol = len(seatMap[0]) - 1
    neighbors = []
    if rownum > 0 and spotNum > 0:
        neighbors.append(seatMap[rownum-1][spotNum-1])
    if rownum > 0 and spotNum < lastCol:
        neighbors.append(seatMap[rownum-1][spotNum+1])
    if rownum > 0:
        neighbors.append(seatMap[rownum-1][spotNum])
    if rownum < lastRow and spotNum > 0:
        neighbors.append(seatMap[rownum+1][spotNum-1])
    if rownum < lastRow and spotNum < lastCol :
        neighbors.append(seatMap[rownum+1][spotNum+1])
    if rownum < lastRow:
        neighbors.append(seatMap[rownum+1][spotNum])
    if spotNum < lastCol:
        neighbors.append(seatMap[rownum][spotNum+1])
    if spotNum > 0:
        neighbors.append(seatMap[rownum][spotNum-1])
    return neighbors


def part2(fileName):
    seatMap = parseInput(fileName)
    iterations = 0
    changes = 1
    while changes != 0:
        seatMap, changes = calculateNextMapPart2(seatMap)
        iterations+=1
    return sum(map(lambda l: l.count(taken), seatMap))

def calculateNextMapPart2(seatMap):
    changes = 0
    height = len(seatMap)
    width = len(seatMap[0])
    newMap = [[i for i in row] for row in seatMap]
    for i in range(height):
        row = seatMap[i]
        for j in range(width):
            spot = row[j]
            adjacentSeats = getNeighborsPart2(seatMap, i, j)
            if spot == seat and not taken in adjacentSeats:
                changes+=1
                newMap[i][j] = taken
            elif spot == taken and adjacentSeats.count(taken) >= 5:
                changes+=1
                newMap[i][j] = seat

    print(changes)
    return (newMap, changes)


def getNeighborsPart2(seatMap, rownum, spotNum):
    lastRow = len(seatMap) - 1
    lastCol = len(seatMap[0]) - 1
    neighbors = []
    for row in (-1, 0, 1):
        for col in (-1, 0, 1):
            if row == 0 and col == 0:
                continue
            spacesOut = 1
            nextRow = rownum + row * spacesOut
            nextCol = spotNum + col * spacesOut
            while 0 <= nextRow <= lastRow and 0 <= nextCol <= lastCol:
                visibleNeighbor = seatMap[nextRow][nextCol]
                if visibleNeighbor != floor:
                    neighbors.append(visibleNeighbor)
                    break
                spacesOut+=1
                nextRow = rownum + row * spacesOut
                nextCol = spotNum + col * spacesOut

    return neighbors





print(part2("input"))