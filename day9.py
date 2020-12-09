def parseInput(fileName):
    numbers = []
    with open(fileName) as f:
        for line in f:
            num = int(line.replace("\n", ""))
            numbers.append(num)

    return numbers

def part1(fileName):
    nums = parseInput(fileName)
    index = 25
    prev25List = nums[:index]
    prev25 = set(prev25List)
    while index < len(nums):
        num = nums[index]
        if (not doLast25Sum(prev25, prev25List, num)):
            return num
        index+=1
        prev25List = nums[index-25:index]
        prev25 = set(prev25List)
    return 0


def doLast25Sum(last25Set, last25List, num):
    for prevNum in last25Set:
        matchNum = num - prevNum
        if matchNum in last25Set and (matchNum != prevNum or prev25List.count(prevNum) > 1):
            return True

    print(last25List, last25Set, num)
    return False

def part2(fileName):
    numberToFind = part1(fileName)
    nums = parseInput(fileName)
    for i in range(len(nums)):
        if (not continousAddsTo(nums, i, numberToFind) == -1):
            return continousAddsTo(nums, i, numberToFind)

def continousAddsTo(nums, firstNumIndex, numToSum):
    index = firstNumIndex
    addsum = 0
    minNum = nums[index]
    maxNum = nums[index]
    while addsum < numToSum:
        num = nums[index]
        maxNum = max(maxNum, num)
        minNum = min(minNum, num)
        if addsum + num == numToSum:
            return minNum + maxNum
        addsum += num
        index+=1
    return -1


print(part2("inputDay9"))