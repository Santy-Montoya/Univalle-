# lista = [1,2,3,4,5]
# for i in lista:
#     print("El valor de:", i)
    

# ejercicio en clase, genera una lista vacia y añade 10 elementos de manera
#aleatorio que sean del 1 al 16 y luego ordenarla de manera ascendente y descende
import random
lista_random = []

for i in range(10):
    lista_random.append(random.randint(1,16))

print(lista_random)
# Ordenar
lista_random.sort()
lista_random.reverse()

print(lista_random)
