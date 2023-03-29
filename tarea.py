bases = {
    2 : ['0','1'],
    3 : ['0','1','2'],
    4 : ['0', '1', '2', '3'],
    5 : ['0', '1', '2', '3', '4'],
    6 : ['0', '1', '2', '3', '4', '5'],
    7 : ['0', '1', '2', '3', '4', '5', '6'],
    8 : ['0', '1', '2', '3', '4', '5', '6', '7'],
    9 : ['0', '1', '2', '3', '4', '5', '6', '7', '8'],
    10 : ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
    11 : ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A'],
    12 : ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B'],
    13 : ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C'],
    14 : ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D'],
    15 : ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E'],
    16 : ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
}

conversion = {
    '0' : 0,
    '1' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    'A' : 10,
    'B' : 11,
    'C' : 12,
    'D' : 13,
    'E' : 14,
    'F' : 15
}

def toDecimal(numStr, base):
    numStr = numStr[::-1]
    numInt = 0
    ind = 0
    while ind < len(numStr):
        numInt += conversion[numStr[ind]] * (base ** ind)
        ind += 1
    
    return(numInt)

def validBinary(numInt, bits):
    range = (2 ** bits) - 1
    if (numInt > range):
        return False
    else:
        return True

def main():
    file = open("numeros.txt")
    bits = int(input('ingrese el tamaño del registro: '))
    numQuant = 0
    base = 0
    baseErrors = 0
    bitsErrors = 0
    numStr = 0
    numInt = 0
    errored = False

    for line in file:
        line = line.strip()
        split_line = line.split("-")
        for i in split_line:
            errored = False
            numInt = 0
            base, numStr = int((i.split(";"))[0]), (i.split(";"))[1] 
            for digit in numStr:
                if digit in bases[base]:
                    print(digit, 'ok')
                else:
                    print(digit, 'notok')
                    errored = True
            if errored:
                baseErrors += 1
            else:
                numInt = toDecimal(numStr, base)
                print(numInt)
                if (validBinary(numInt, bits)):
                    print(numInt, 'representable')
                else:
                    print(numInt, 'nope')
                    bitsErrors += 1
                    
            
            
            
                    
        numQuant += 2

    print(numQuant, baseErrors, bitsErrors)
    file.close()


if __name__ == "__main__":
    main()
