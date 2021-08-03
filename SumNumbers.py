#Programa que suma los valores ingresados

def sums(num1, num2):
    result = num1 + num2
    return result

def printSums():
    valor1 = int(input("Ingrese el primer valor: \n"))
    valor2 = int(input("Ingres el segundo valor: \n"))
    print("La suma de los numeros dados es: ", sums(valor1, valor2))

printSums()