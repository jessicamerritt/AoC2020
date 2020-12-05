def parseInput(fileName):
    rows = []
    with open(fileName) as f:
        for line in f:
            rows.append(line)

    return rows

def problem1(fileName):
    bPass = parseInput(fileName)
    maxId = 0
    for entry in bPass:
        row = getRow(entry)
        seat = getSeat(entry)
        seatId = row * 8 + seat
        if seatId > maxId:
            maxId = seatId
    return maxId


def getRow(entry):
    rowString = entry[:7].replace("F", "0").replace("B", "1")
    return int(rowString, 2)

def getSeat(entry):
    seatString = entry[7:].replace("L", "0").replace("R", "1")
    return int(seatString, 2)

def problem2(fileName):
    bPass = parseInput(fileName)
    rowsWithMissingSeats = {}
    lastRow = 0
    for entry in bPass:
        row = getRow(entry)
        lastRow = max(lastRow, row)
        seat = getSeat(entry)
        seatId = row * 8 + seat
        if row not in rowsWithMissingSeats:
            rowsWithMissingSeats[row] = [seat]
        elif len(rowsWithMissingSeats[row]) == 7:
            #remove the row it's full
            del rowsWithMissingSeats[row]
        else:
            rowsWithMissingSeats[row].append(seat)
    #remove first and last row
    del rowsWithMissingSeats[1]
    del rowsWithMissingSeats[lastRow]
    return(findMissingSeatId(rowsWithMissingSeats))
    print(rowsWithMissingSeats)

def findMissingSeatId(rowMap):
    for key, value in rowMap.items():
        for i in range(8):
            seat = i + 1;
            if not seat in value:
                print(value, seat)
                return key * 8 + seat


print(problem2("inputDay5"))

