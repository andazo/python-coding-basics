from SumNumbers import printSums


#Incremento del valor ingresado

def incrementValue(val):
    val += 1
    return val

def printValue():
    valor = int(input("Digite el valor deseado: \n"))
    print("Resultado: ", incrementValue(valor))
    
printValue()