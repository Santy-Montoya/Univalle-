print("--------------------------------------------------------")
print("Por favor ingrese los siguientes datos:")

""" name = input("Nombre: ")
last_name = input("Apellido: ")
type_documen = input("Tipo de documento de identidad: ")
document_number = input("Número de documento de identidad")
date_born = input("Fecha de nacimiento")
city_born = input("Ciudad de nacimiento")
dirc_res = input("Dirección de residencia") """
cantidad_familiares = int(input("Cantidad de familiares a registrar"))

print()
print("--------------------------------------------------------")

familiares = []

for i in range(5):
    familiar = []
    familiar.append(input("Nombre: ")) 
    familiar.append(input("Apellido: "))
    familiar.append(input("Tipo de documento de identidad: "))
    familiar.append(input("Número de documento de identidad: "))
    familiar.append(input("Fecha de nacimiento: "))

    familiares.append(familiar)

    print("--------------------------------------------------------")
     
