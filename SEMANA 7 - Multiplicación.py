# inicio = 3
# while inicio <= 7:
#     print("tabla del " + str(inicio) )
#     inicio2 = 1
#     while inicio2 <= 10:
#          print(str(inicio) + "X"+ str(inicio2) + "=" + str(inicio  * inicio2))
#          inicio2 += 1 
#     inicio += 1
 
inicio = 2 
resultado = 0
acumulador = 0
while inicio <= 11:
    print("tabla del "+ str(inicio))
    proceso = 1
    acumulador=0
    while proceso <= 12:
        resultado = inicio * proceso
        print (inicio, " X " , proceso , "=" , resultado)
        
        proceso += 1
        acumulador += resultado
    print(f"Total de la tabla {inicio}: {acumulador}")
    inicio += 1