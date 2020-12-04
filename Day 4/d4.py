essentialFields=['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def isValidPasswordPart1(password):
    for field in essentialFields:
        if not (field in password):
            return False
    return True

def isValidPasswordPart2(password):
    if not isValidPasswordPart1(password):
        return False

    password=password.replace(':', ' ').strip().split()
    for i in range(0, len(password), 2):
        if password[i] == 'byr':
            if len(password[i+1])!=4 or not (int(password[i+1]) in range(1920, 2003)):
                return False
        elif password[i] == 'iyr':
            if len(password[i+1])!=4 or not (int(password[i+1]) in range(2010, 2021)):
                return False
        elif password[i] == 'eyr':
            if len(password[i+1])!=4 or not (int(password[i+1]) in range(2020, 2031)):
                return False
        elif password[i] == 'hgt':
            if 'cm' in password[i+1]:
                currentHeight=password[i+1].replace('cm', '')
                if not (int(currentHeight) in range(150, 194)):
                    return False
            elif 'in' in password[i+1]:
                currentHeight=password[i+1].replace('in', '')
                if not (int(currentHeight) in range(59, 77)):
                    return False
            else:
                return False
        elif password[i] == 'hcl':
            if password[i+1][0] != '#' or not password[i+1][1:].isalnum():
                return False
        elif password[i] == 'ecl':
            colors=['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            if not (password[i+1] in colors):
                return False
        elif password[i] == 'pid':
            if len(password[i+1]) != 9 or not(password[i+1].isnumeric()):
                return False
    return True

def partOne():
    with open("input.txt", "r") as inputFile:
        data=inputFile.read().split('\n\n')
        countValidPasswords=0
        for password in data:
            password=password.replace('\n', ' ')
            if isValidPasswordPart1(password):
                countValidPasswords+=1
        return countValidPasswords


def partTwo():
    with open("input.txt", "r") as inputFile:
        data=inputFile.read().split('\n\n')
        countValidPasswords=0
        for password in data:
            password=password.replace('\n', ' ')
            if isValidPasswordPart2(password):
                countValidPasswords+=1
        return countValidPasswords

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
