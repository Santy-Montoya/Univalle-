#### INVESTIGACION ############    

lista=[]#lista vacia, se le pueden agregar, sumar y literanmente utilizar para muchas cosas

lista = ["lunes", "martes" , "miercoles", "jueves", "viernes" , 30 , 5.96, [3, 5, 6], True]

tol = len(lista)
print(tol)
print(lista[7][1])#buscar una lista dentro de una lista

lista2 = [1,2,4,5,6,7,8,9,]

lista2.append(10) #insertar al final de la lista
print(lista2)

lista2.insert(2,3)  #insertar en un lugar especifico de la lista (luagr : lo que quiero insertar)
print(lista2)

lista2.extend([11,12,13,14,15]) #agregar  a una lista 
print(lista2)

lista3 = lista + lista2 #sumar listas 
print(lista3)
       
lista = [2, -3, 15, 0, 78, 11] 
lista.sort(reverse=True) #ordena decendentemente

lista.sort() #ordena acendentemente

lista.reverse() #voltea la lista

lista.clear()  #elimina la lista por completo

lista.remove(1) #elimina el elemento deseado 

lista.pop() # busca y elimina el indice deseado
print(lista)
print(6 in lista ) #buscar en la lista

print(lista.index(2)) #en que lugar de la lista esta 
print(lista.count(3)) #contar cuantas veces esta el elemnto

lista=[2, 4, 5, 8, 9, 10]
print(lista[0:6])#imprimir un rango dentro de una lista
print(lista[0], lista [5])#imprimir elemntos de una lista por separado
lista2=lista[1:4]#asignar un pedazo de la lista a una variable
print(lista2)