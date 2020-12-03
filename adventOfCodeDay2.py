
def parseInput(fileName):
    passwordRuleEntries = []
    with open(fileName) as f:
        for line in f:
            passwordRule = line.split(":")[0]
            letter = passwordRule.split(" ")[1]
            minNum = passwordRule.split("-")[0]
            maxNum = passwordRule.split(" ")[0].split("-")[1]
            password = line.split(":")[1][1:]

            passwordRuleEntries.append(PasswordRuleAndEntry(letter, minNum, maxNum, password))

    return passwordRuleEntries

class PasswordRuleAndEntry:
    def __init__(self, letter, minNum, maxNum, password):
         self.letter = letter
         self.minNum = minNum
         self.maxNum = maxNum
         self.password = password

def problem1(fileName):
    entries = parseInput(fileName)
    total = 0
    for e in entries:
        validPassword = int(e.minNum) <= e.password.count(e.letter) and e.password.count(e.letter) <= int(e.maxNum)
        if validPassword:
            total+=1

    print(total)


def problem2(fileName):
    entries = parseInput(fileName)
    total = 0
    for e in entries:
        password = e.password
        try:
            charsAtIndex = [password[int(e.minNum)-1], password[int(e.maxNum)-1]]
            if (charsAtIndex.count(e.letter) == 1):
                total+=1
        except:
            print("______________________________")
            print("maxNum = " + e.maxNum)
            print("password len = " + str(len(password)))
            print(password)

    print(total)

problem2("DayTwoProblem1Input")