lista = [1, 2, 3, "America"]
lista2 = [4, 5, "HALLOWEN"]

# SUMA DE LISTAS:
lista12 = lista + lista2 
#print(lista12)

# Lista en slice
#print(lista12[1:4])


list_slice = lista12[1:4]

#print(list_slice)

list_slice.extend(lista)
#print(list_slice)

# Miltipliacion de listas 
list4 = lista[3] * 16
#print(list4)

# Eliminar el ultimo elemento de la lista 

lista5 = lista.pop(0)
#print(lista)

# Ordernar  la lista
list = [4,5,6,7,8,22,3,1,4,]
lista_text = ["a", "o", "e", "r", "w", "t"]
lista6 = list.sort()
lista7 = lista_text.sort()
print(list, lista_text)


