def parseInput(fileName):
    with open(fileName) as file:
        string = file.read()
        timestamp = string.split("\n")[0]
        busIds = string.split("\n")[1].split(",")

        return int(timestamp), busIds

def problem1(fileName):
    timestamp, busIds = parseInput(fileName)
    minwait = 9999999
    minid = -1
    for bus in busIds:
        if bus != ("x"):
            wait = (-timestamp) % int(bus)
            if (wait < minwait) :
                minwait = wait
                minid = int(bus)
    print(minid, minwait)
    return minid * minwait





def problem2(fileName):
    timestamp, busIds = parseInput(fileName)
    start = int(busIds[0])
    index = 0
    timestamp = int(busIds[0])
    jumpBy = 1
    #find x such that  x + index % busid at index = 0
    # inputs are prime numbers so we can loop intelligently
    for index in range(len(busIds)):
        bus = busIds[index]
        if bus != "x":
            bus = int(bus)
            while not (timestamp + index) % bus == 0:
                timestamp = timestamp + jumpBy
            jumpBy *= bus
    return timestamp








print(problem2("input"))

