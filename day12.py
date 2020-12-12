def parseInput(fileName):
    rows = []
    with open(fileName) as f:
        for line in f:
            l = line.replace("\n", "")
            rows.append(l)

    return rows

def problem1(fileName):
    instructions = parseInput(fileName)
    direction = 90
    dLetter = "E"
    startx = 0
    starty = 0
    for instruction in instructions:
        print(direction, dLetter)
        letter = instruction[0]
        num = int(instruction[1:])
        if letter == "F":
            letter = dLetter
        if letter == "N":
            starty += num
        if letter == "S":
            starty -= num
        if letter == "E":
            startx += num
        if letter == "W":
            startx -= num
        if letter == "L":
            direction = (direction - num) % 360
        if letter == "R":
            direction = (direction + num) % 360
        if direction == 0:
            dLetter = 'N'
        if direction == 90:
            dLetter = 'E'
        if direction == 180:
            dLetter = 'S'
        if direction == 270:
            dLetter = 'W'
    return abs(startx) + abs(starty)


    return maxId


def problem2(fileName):
    instructions = parseInput(fileName)
    startx = 0
    starty = 0
    wayx = 10
    wayy = 1
    for instruction in instructions:
        letter = instruction[0]
        num = int(instruction[1:])
        if letter == "F":
            startx += (wayx * num)
            starty += (wayy * num)
        if letter == "N":
            wayy += num
        if letter == "S":
            wayy -= num
        if letter == "E":
            wayx += num
        if letter == "W":
            wayx -= num
        if letter == "L":
            # 90 goes xy -> -y,x
            # 180 goes to -x, -y
            # 270 goes to y, -x
            degrees = num % 360
            if degrees == 90:
                wayx, wayy = -wayy, wayx
            if degrees == 180:
                wayx, wayy = -wayx, -wayy
            if degrees == 270:
                wayx, wayy = wayy, -wayx


        if letter == "R":
            degrees = (-num) % 360
            if degrees == 90:
                wayx, wayy = -wayy, wayx
            if degrees == 180:
                wayx = -wayx
                wayy = -wayy
            if degrees == 270:
                wayx, wayy = wayy, -wayx
    return abs(startx) + abs(starty)



print(problem2("input"))

