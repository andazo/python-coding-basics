def calculator(num1, operation, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/" and num2 == 0:
        print("No se puede dividir entre 0")
    elif operation == "/":
        return num1 / num2

calculator(5,"-",5)