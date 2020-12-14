import itertools 

def applyMask(mask, integer):
    binary=str(bin(integer))[2:]
    binary=['0']* (len(mask) - len(binary)) + [b for b in binary]
    for bit in range(len(mask)):
        if mask[bit] == '0':
           binary[bit] = '0'
        elif mask[bit] == '1':
            binary[bit] = '1'
    return int(''.join(binary), 2)

def partOne():
    with open("input.txt", "r") as inputFile:
        mask = '0'
        mem = {}
        for line in inputFile:
            if 'mask' in line:
                mask = line.strip().replace('mask = ', '')
            elif 'mem' in line:
                address , value = line.strip().replace('mem', '').replace('[', '').replace('] =', '').split()
                mem[int(address)] = applyMask(mask, int(value))

        return sum(mem.values())

def getAddresses(mask, address):
    address=str(bin(int(address)))[2:]
    address=['0']* (len(mask) - len(address)) + [b for b in address]

    addresses=[]
    floatingBits=[]
    for bit in range(len(mask)):
        if mask[bit] == '1':
            address[bit] = '1'
        elif mask[bit] == 'X':
            floatingBits.append(bit)

    prod=itertools.product(['0', '1'], repeat=len(floatingBits))
    for p in prod:
        for i in range(len(floatingBits)):
            address[floatingBits[i]]=p[i]
        addresses.append(int(''.join(address), 2))
    return addresses

def partTwo():
    with open("input.txt", "r") as inputFile:
        mask = '0'
        mem = {}
        for line in inputFile:
            if 'mask' in line:
                mask = line.strip().replace('mask = ', '')
            elif 'mem' in line:
                address , value = line.strip().replace('mem', '').replace('[', '').replace('] =', '').split()
                addresses = getAddresses(mask, address)
                for ad in addresses:
                    mem[ad] = int(value)

        return sum(mem.values())

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
