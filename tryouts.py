bases = {
    "2" : ["0","1"],
    "3" : ["0","1","2"],
    "4" : ["0","1","2","3"],
    "5" : ["0","1","2","3","4"],
    "6" : ["0","1","2","3","4","5"],
    "7" : ["0","1","2","3","4","5","6"],
    "8" : ["0","1","2","3","4","5","6","7"],
    "9" : ["0","1","2","3","4","5","6","7","8"],
    "10" : ["0","1","2","3","4","5","6","7","8","9"],
    "11" : ["0","1","2","3","4","5","6","7","8","9","A"],
    "12" : ["0","1","2","3","4","5","6","7","8","9","A","B"],
    "13" : ["0","1","2","3","4","5","6","7","8","9","A","B","C"],
    "14" : ["0","1","2","3","4","5","6","7","8","9","A","B","C","D"],
    "15" : ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E"],
    "16" : ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
}
conversion = {
    "0" : 0,
    "1" : 1,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "A" : 10,
    "B" : 11,
    "C" : 12,
    "D" : 13,
    "E" : 14,
    "F" : 15,
}
numeros_bases = []
numbers = {}

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

def toDecimal(numStr, base):
    numStr = numStr[::-1]
    numInt = 0
    ind = 0
    while ind < len(numStr):
        numInt += int(conversion[numStr[ind]]) * (int(base) ** ind)
        ind += 1
    return(numInt)

def toBinary(number):
    binary = ""
    while number > 0:
        remainder = int(number % 2)
        number = int(number / 2)
        binary = str(remainder  ) + binary
    return binary

def comprobar_base(numero, base):
    for i in range(len(numero)):
        if bases[base].count(numero[i]) == 0:
            return False            
    return True

def sign_extension(number, register):
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
        sum+="1"
    sum = sum[::-1]
    return sum


try:
    salida = open("resultados.txt", "x")
    salida.close()
except FileExistsError:

    pass

archivo = open("numeros.txt","r")
lineas = archivo.readlines()

for linea in lineas:
    t1,t2 = linea.strip().split("-")
    base1,num1 = t1.split(";")
    base2,num2 = t2.split(";")
    numeros_bases.append((num1,base1))
    numeros_bases.append((num2,base2))

x = 1
while x <= len(numeros_bases):
    numbers[x] = [numeros_bases[x-1][0],numeros_bases[x-1][1]]
    x+=1
x-=1

archivo.close()

# Programa principal

while True:
    register = int(input("Ingrese tamaño de registro: "))
    if register == 0:
        salida = open("resultados.txt", "r")
        aux = salida.readlines()
        mistakes = 0
        for i in aux:
            _,b,c,d = i.strip().split(";")
            mistakes = mistakes + int(b) + int(c) + int(d.strip("."))
        salida.close()
        if mistakes > x:
            print("Los errores son mayor a la cantidad de numeros, programa finalizado")
            exit()
        elif mistakes < x:
            print("Registro valido. Vuelva a ingresar otro")
    else:
        list_aux = []
        i = 1
        while i <=  x:
            aux = numbers[i]
            aux.append(comprobar_base(aux[0], aux[1]))
            if aux[2]:
                aux.append(toDecimal(aux[0],aux[1]))
                aux.append(toBinary(aux[3]))
            else:
                aux.append("Base Invalida")    
                aux.append("Base Invalida")   
            list_aux.append(aux)
            i+=1
        parte_b = 0
        parte_c = 0
        parte_d = 0

        for u in list_aux:
            if u[2]:
                if validBinary(u[3],register):
                    u.append(sign_extension(u[4],register))
                    
                else:   
                    parte_c += 1
                    u.append("Error")
            else:
                parte_b += 1
                u.append("Error")
            print(u)

        flag = True
        x,y = 0,1
        while flag:
            if list_aux[x][5] == "Error" or list_aux[y][5] == "Error":
                x+=2
                y+=2
                if y > len(list_aux):
                    flag = False
            else:
                if register < len(sum_C2(toC2(list_aux[x][5]),toC2(list_aux[y][5]))):
                    parte_d += 1
                x+=2
                y+=2
                if y > len(list_aux):
                    flag = False

        file = open("resultados.txt","a")
        file.write( str(x)+";"+str(parte_b)+";"+str(parte_c)+";"+str(parte_d)+".\n")
        file.close()
        
        o = 0
        for o in range(len(numeros_bases)):
            numbers[o+1] = [numeros_bases[o][0],numeros_bases[o][1]]
        
        print(x, parte_b, parte_c, parte_d)
        print(numbers)
