BASES = {
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

CONVERSION = {
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
        numInt += int(CONVERSION[numStr[ind]]) * (int(base) ** ind)
        ind += 1
    return(numInt)


def validBinary(numInt, bits):
    range = (2 ** bits) - 1
    if (numInt > range):
        return False
    else:
        return True
    

def toC2(number):
    new_binary = ""

    for i in range(len(number)):
        if number[i] =="0":
            new_binary += "1"
        elif number[i] == "1":
            new_binary += "0"
    
    new_binary = new_binary[::-1]

    new_binary2 = ""
    remainder = "1"

    for i in range(len(new_binary)):
        if new_binary[i] == "1" and remainder == "1":
            new_binary2 += "0"
            remainder = "1"
        elif new_binary[i] == "1" and remainder == "0":
            new_binary2 += "1"
            remainder = "0"
        elif new_binary[i] == "0" and remainder == "1":
            new_binary2 += "1"
            remainder = "0"
        elif new_binary[i] == "0" and remainder == "0":
            new_binary2 += "0"
            remainder = "0"

    new_binary2 = new_binary2[::-1]

    return new_binary2


def toBinary(number):
    binary = ""
    while number > 0:
        remainder = int(number % 2)
        number = int(number / 2)
        binary = str(remainder  ) + binary
    return binary


def checkBase(number, base):
    for i in range(len(number)):
        if BASES[int(base)].count(number[i]) == 0:
            return False            
    return True


def signExtension(number, register):
    if len(number) == register:
        return number
    else:
        while len(number) != register:
            number = number[0] + number
        return number
    

def sum_C2(number1, number2):
    aux1 = number1[::-1]
    aux2 = number2[::-1]
    sum = ""
    remainder = "0"

    for i in range(len(number1)):
        if aux1[i] == "1" and aux2[i] == "1" and remainder == "1":
            sum += "1"
            remainder = "1"
        elif aux1[i] == "1" and aux2[i] == "1" and remainder == "0":
            sum += "0"
            remainder = "1"
        elif aux1[i] == "1" and aux2[i] == "0" and remainder == "1":
            sum += "0"
            remainder = "1"
        elif aux1[i] == "1" and aux2[i] == "0" and remainder == "0":
            sum += "1"
            remainder = "0"
        elif aux1[i] == "0" and aux2[i] == "1" and remainder == "1":
            sum += "0"
            remainder = "1"
        elif aux1[i] == "0" and aux2[i] == "1" and remainder == "0":
            sum += "1"
            remainder = "0"
        elif aux1[i] == "0" and aux2[i] == "0" and remainder == "1":
            sum += "1"
            remainder = "0"
        elif aux1[i] == "0" and aux2[i] == "0" and remainder == "0":
            sum += "0"
            remainder = "0"    
   
    if remainder == "1":
        sum += "1"
    sum = sum[::-1]
    return sum


def main():
    inFile = open("numeros.txt")
    lines = inFile.readlines()
    numsBases = []
    numbers = {}

    try:
        outFile = open("resultados.txt", "x")
        outFile.close()
    except FileExistsError:

        pass

    for line in lines:
        t1,t2 = line.strip().split("-")
        base1,num1 = t1.split(";")
        base2,num2 = t2.split(";")
        numsBases.append((num1, base1))
        numsBases.append((num2, base2))

    numQuant = 1
    while numQuant <= len(numsBases):
        numbers[numQuant] = [numsBases[numQuant - 1][0],numsBases[numQuant - 1][1]]
        numQuant += 1
    numQuant -= 1

    inFile.close()

    
    while True:
        regSize = int(input('Ingrese el tamaño del registro: '))
        
        if regSize == 0:
            outFile = open("resultados.txt", "r")
            aux = outFile.readlines()
            totalErrors = 0

            for i in aux:
                _, b, c, d = i.strip().split(";")
                totalErrors += int(b) + int(c) + int(d.strip("."))
            outFile.close()

            if totalErrors > numQuant:
                print("La cantidad de errores es mayor al tamaño del registro, finalizando programa.")
                return
            else:
                print("Tamaño de registro válido.")

        else:
            auxList = []
            i = 1

            while i <=  numQuant:
                aux = numbers[i]
                aux.append(checkBase(aux[0], aux[1]))

                if aux[2]:
                    aux.append(toDecimal(aux[0],aux[1]))
                    aux.append(toBinary(aux[3]))
                else:
                    aux.append("Base Invalida")    
                    aux.append("Base Invalida")   

                auxList.append(aux)
                i += 1

            baseErrors = 0
            bitsErrors = 0
            overflow = 0

            for u in auxList:
                if u[2]:
                    if validBinary(u[3],regSize):
                        u.append(signExtension(u[4],regSize))  
                    else:   
                        bitsErrors += 1
                        u.append("Error")

                else:
                    baseErrors += 1
                    u.append("Error")

                print(u)

            flag = True
            x,y = 0,1

            while flag:
                if auxList[x][5] == "Error" or auxList[y][5] == "Error":
                    x += 2
                    y += 2

                    if y > len(auxList):
                        flag = False

                else:
                    if regSize < len(sum_C2(toC2(auxList[x][5]),toC2(auxList[y][5]))):
                        overflow += 1
                    x += 2
                    y += 2

                    if y > len(auxList):
                        flag = False

            file = open("resultados.txt","a")
            file.write( str(x) + ";" + str(baseErrors) + ";" + str(bitsErrors) + ";" + str(overflow) + ".\n")
            file.close()
            
            o = 0
            for o in range(len(numsBases)):
                numbers[o + 1] = [numsBases[o][0],numsBases[o][1]]
            
            print(numQuant, baseErrors, bitsErrors, overflow)
            print(numbers)

if __name__ == "__main__":
    main()