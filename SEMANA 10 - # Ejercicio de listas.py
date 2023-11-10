# Ejercicio de listas 

#1
# def pedirdatos (lista):
    
#     materias = str(input("Ingrese materia: "))
#     lista.append(materias)
#     return lista 

# if __name__ == '__main__':

#     lista = []
#     for i in range (0,6):
#          pedirdatos(lista)
#     print(lista)

#2
def pedirdatos (lista):
    
    materias = str(input("Ingrese materia: "))
    lista.append(materias)
    return lista 

if __name__ == '__main__':

    lista = ['matematicas', 'ingles', 'historia', 'deporte y salud', 'insercion']

    for i in range (0,5):
         print ("yo estudio la materia: " + lista[i])

#3 

def nota ():
    nota = float(input("Ingrese la nota de la asignatura: "))