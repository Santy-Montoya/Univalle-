
# Tuplas 
tupla1 = (2,12, "America", (16,27), "B", 20231567)
#print(tupla1, type(tupla1))


# acceder a los elementos de una Tupla
#for i in range(len(tupla1)): # 0,1,2,3,4
    #print(tupla1[i])

#print(tupla1[0], tupla1[3], tupla1[5])

#Reasignar una tupla (copiarla)

tupla2 = (16, "America", "Nacional", "Millonarios", "Medellin")
tupla1 += tupla2
print(tupla1)

# Métodos con tuplas
print(tupla1.count(16))
print(tupla1.index("America"))
#Ejercicio en casa, recorrer todos los elemntos de la tupla y devolver los índices de la palabra america

print(dir(tupla1))
print(id(tupla1))