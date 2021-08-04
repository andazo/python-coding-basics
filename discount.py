def findDiscount(value,dic):
    finalValue = value * (100 - dic) * 0.01
    return finalValue

def printDiscount():
    valueProduct = int(input("Ingrese el valor del producto \n"))
    discountProduct = int(input("Ingrese el descuento del producto \n"))
    print("El precio final del producto despues de aplicar el descuento es de: ", findDiscount(valueProduct,discountProduct))

printDiscount()


