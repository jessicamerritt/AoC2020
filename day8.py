def parseInput(fileName):
    lines = []
    with open(fileName) as f:
        for line in f:
            operation, signedNum = line.split(" ")
            num = signedNum.replace("\n", "")
            lines.append(Instruction(operation, int(signedNum)))

    return lines

class Instruction:
    def __init__(self, operation, number):
        self.operation = operation
        self.number = number

def part1(fileName):
    instructions = parseInput(fileName)
    visted = set()
    index = 0
    acc = 0
    while not index in visted and not index >= len(instructions):
        visted.add(index)
        instruction = instructions[index]
        op = instruction.operation
        if op == "acc":
            index += 1
            acc += instruction.number
        elif op == "jmp":
            index += instruction.number
        else:
            index +=1
    return acc

def getAccForInput(instructions):
    visted = set()
    index = 0
    acc = 0
    while not index in visted and not index >= len(instructions):
        visted.add(index)
        instruction = instructions[index]
        op = instruction.operation
        if op == "acc":
            index += 1
            acc += instruction.number
        elif op == "jmp":
            index += instruction.number
        else:
            index +=1
    return acc

def itLoops(instructions):
    visted = set()
    index = 0
    while not index in visted and not index > len(instructions) and not index > len(instructions):
        if index == len(instructions):
            return False
        visted.add(index)
        instruction = instructions[index]
        op = instruction.operation
        print(instruction.number, op, index)
        if op == "acc":
            index += 1
        elif op == "jmp":
            index += instruction.number
        else:
            index +=1
    return True

def part2(fileName):
    instructions = parseInput(fileName)
    index = 0
    for line in instructions:
        op = line.operation
        if op == "acc":
            index+=1
            continue
        elif op == "jmp":
            op = "nop"
        else:
           op = "jmp"
        newInst = instructions[:]
        newInst[index] = Instruction(op, line.number)

        if not (itLoops(newInst)):
            return getAccForInput(newInst)

        index +=1
    return 0



print(part2("inputDay8"))