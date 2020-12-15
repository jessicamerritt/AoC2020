import collections

startingNums = [0,20,7,16,1,18,15]

def problem1(startingNums, endNum):
    turnMap = {}
    countMap = collections.defaultdict(int)
    for i in range(len(startingNums)):
        num = startingNums[i]
        turnMap[num] = i
        countMap[num] += 1
    lastNum = startingNums[len(startingNums) - 1]
    turnNum = len(startingNums)
    for i in range(turnNum, endNum):
        if countMap[lastNum] > 1:
            print(i, turnMap[lastNum])
            newNum = i - 1 - turnMap[lastNum]
            countMap[newNum] += 1
            turnMap[lastNum] = i - 1
            lastNum = newNum
        else:
            newNum = 0
            turnMap[lastNum] = i -1
            countMap[newNum] += 1
            lastNum = newNum
    return lastNum


print(problem1(startingNums, 30000000))

