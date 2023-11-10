# x = float(input("digite por favor un numero"))
# y = (((3*((x)**3)))-(2*((x)**2))+(3*x))-1
# print(y)

peso = float(input("digite por favor su peso en kg: "))
estatura = float(input("digite por favor su estatura  en mts"))
imc = peso / (estatura)**2
if imc <=18.5:
    print ("el índice de su masa corporal es de",imc, " y su estado de obecidad es de: Bajo peso")
if imc  >= 18.5 and imc <= 24.9:
    print ("el índice de su masa corporal es de",imc, " y su estado de obecidad es de: Peso normal")
if imc  >= 25.0 and imc <= 29.9:
    print ("el índice de su masa corporal es de",imc, " y su estado de obecidad es de: Sobrepeso")
if imc >=30.0:
    print ("el índice de su masa corporal es de",imc, " y su estado de obecidad es de: Obesidad tipo 1")


