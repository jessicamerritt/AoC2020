def parseInput(fileName):
    numbers = []
    with open(fileName) as f:
        for line in f:
            num = int(line.replace("\n", ""))
            numbers.append(num)

    return numbers

def part1(fileName):
    nums = parseInput(fileName)
    nums.sort()
    diffCountMap = {0:0, 1:0, 2:0, 3:1}
    lastNum = 0
    for num in nums:
        diffCountMap[num - lastNum] += 1
        lastNum = num

    return diffCountMap[3] *  diffCountMap[1]


def part2(fileName):
    nums = parseInput(fileName)
    nums.sort()
    posJumpMap = {nums[0] : 1}

    #every value can be used we know that from part one
    for num in nums:
        if (num <= 3) :
            posJumpMap[num] = 1
        else:
            posJumpMap[num] = 0
        for i in range(max(num-3, 0),num):
            if i in nums:
                posJumpMap[num] += posJumpMap[i] 
    print(posJumpMap)




print(part2("input"))