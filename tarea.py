# from os import remove
# remove("resultados.txt")

BASES = {
    "2" : ['0','1'],
    "3" : ['0','1','2'],
    "4" : ['0', '1', '2', '3'],
    "5" : ['0', '1', '2', '3', '4'],
    "6" : ['0', '1', '2', '3', '4', '5'],
    "7" : ['0', '1', '2', '3', '4', '5', '6'],
    "8" : ['0', '1', '2', '3', '4', '5', '6', '7'],
    "9" : ['0', '1', '2', '3', '4', '5', '6', '7', '8'],
    "10" : ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
    "11" : ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A'],
    "12" : ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B'],
    "13" : ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C'],
    "14" : ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D'],
    "15" : ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E'],
    "16" : ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
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
    """
    Convierte un número desde cualquier base a base 10.

    Usando el mismo algoritmo visto en clases, convierte cualquier número en cualquier base a un número en base 10.

    Parameters
    ----------
    numStr : str
        Número a convertir, en formato string.
    base : str
        Base en la que está el número a convertir.

    Returns
    -------
    int
        Número convertido a base 10

    """
    numStr = numStr[::-1]
    numInt = 0
    ind = 0
    while ind < len(numStr):
        numInt += int(CONVERSION[numStr[ind]]) * (int(base) ** ind)
        ind += 1
    return(numInt)


def validBinary(numInt, bits):
    """
    Revisa si el número se puede escribir en binario con la cantidad de bits dada.

    Revisa si el número está dentro del rango permitido para un número binario con la cantidad de bits dada.

    Parameters
    ----------
    numInt : int
        Número a revisar.
    bits : int
        Cantidad de bits.

    Returns
    -------
    bool
        Retorna True si es posible representarlo, y False en caso contrario.

    """
    range = (2 ** bits) - 1
    if (numInt > range):
        return False
    else:
        return True
    

def toC2(number):
    """
    Transforma un numero binario a su version en complemento de dos.
    
    Toma la representacion de un numero binario y la pasa a complemnto dos de siguiendo los pasos:
    - Transformar a C1
    - sumarle uno en binario
    
    Parameters
    ----------
    number : string
        representacion del numero que se quiere convertir.

    Returns
    -------
    string
        Complemento dos del numero introducido.
    
    """
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
    """
    Transforma un numero a su representación en binario.
    
    Toma un numero en base 10, y lo transforma en su version en binario.

    Parameters
    ----------
    number : int
        Representación del numero en base 10.

    Returns
    -------
    String
        Representación en binario del numero introducido.
    
    """
    binary = ""
    while number > 0:
        remainder = int(number % 2)
        number = int(number / 2)
        binary = str(remainder) + binary
    return binary


def checkBase(numStr, base):
    """
    Revisa si el número se puede representar en la base dada.

    Revisa si cada dígito está dentro de los dígitos permitidos en la base.

    Parameters
    ----------
    numStr : str
        Número a revisar, en formato string.
    base : str
        Base a revisar.

    Returns
    -------
    bool
        False, si algún dígito no está en la base, True en caso contrario.

    """
    for digit in numStr:
        if digit not in BASES[base]:
            return False            
    return True


def signExtension(number, register):
    """
    Permite hacer la extensión de signo si es requerida.

    Toma la representación de un numero binario de n bits y le hace la extension de signo hasta
    el tamaño del registro querido.

    Parameters
    ----------
    number : String
        Representación del numero en binario
    register : int
        Tamaño del registro del numero
    
    Returns
    -------
    String
        Numero en binario con la extensión de signo si es que fue hecha.
    
    """
    if len(number) == register:
        return number
    else:
        while len(number) != register:
            number = number[0] + number
        return number
    

def sum_C2(number1, number2):
    """
    Suma los complemento dos.
    
    Realiza la suma de dos numeros binarios que están en complemento dos.
    
    Parameters
    ----------
    number1: String
        Representación del complemento 2 de un numero binario
    number2: String
        Representación del complemento 2 de un numero binario

    Returns
    -------
    String
        La representación de la suma de los dos numeros introducidos.
    
    """
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
                print("Tamaño de registro válido (La cantidad de errores no supera la cantidad de numeros del archivo).")

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

if __name__ == "__main__":
    main()