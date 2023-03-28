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

def toDecimal(numStr, base):
    numStr = numStr[::-1]
    numInt = 0
    ind = 0
    while ind < len(numStr):
        numInt += conversion[numStr[ind]] * (base ** ind)
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
print("11011")
print(sign_extension("11011",5))

archivo = open("numeros.txt","r")
lineas = archivo.readlines()


for linea in lineas:
    t1,t2 = linea.strip().split("-")
    base1,num1 = t1.split(";")
    base2,num2 = t2.split(";")
    numeros_bases.append((num1,base1))
    numeros_bases.append((num2,base2))

archivo.close()

parte_B = 0
for i in range(len(numeros_bases)):
    if not comprobar_base(numeros_bases[i][0],numeros_bases[i][1]):
        parte_B +=1

# register = int(input("Ingrese tamaño de resgistro: "))

# if register == 0:
#     try:
#         f = open("resultados.txt", "x")
#         errores = 0 
#         print("Registro valido, ingrese otro valor:\n")
#         register = int(input("Ingrese tamaño de resgistro: "))
#     except FileExistsError:
#         f = open("resultados.txt", "r")


# guardar numeros , crear "resultados.txt"
# pedir numeros de registro, hacer validaciones