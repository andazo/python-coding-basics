#Conversor minutos a segundos

def conversor(min):
    resultado = min * 60
    return resultado

def printConversion():
    minutos = int(input("Digite los minutos deseados: \n"))
    print(minutos, " minutos equivalen a ", conversor(minutos), " segundos")

printConversion()