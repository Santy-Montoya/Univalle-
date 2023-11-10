def divicion ():
    try:
        num1 = int(input("Digite por favor un numero: "))
        num2 = int (input("Digite por favor otro numero: "))
        print("la divición es:", num1 / num2)
    except ZeroDivisionError:
        print(" No es posible dividir por cero")
        divicion()
divicion()