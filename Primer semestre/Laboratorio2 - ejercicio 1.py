
# global nombre 
# global peso 
# global altura

# def masa_corporal():
#     nombre = input("Por favor ingresar su nombre y apellido: ")
#     peso = int(input("Por favor ingresar su peso en kg: "))
#     altura = float(input("Por favor ingresar su altura en Mts: "))
#     imc =  peso/(altura ** 2)
#     if imc < 18.5:
#         print("Su indice de masa corporal es: ", imc, "y su categoria es: Infrapeso")
#     elif 

# masa_corporal()

# Función para calcular el IMC y determinar la categoría

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        categoria = "Infrapeso"
    elif 18.5 <= imc < 24.9:
        categoria = "Normal"
    else:
        categoria = "Sobrepeso"
    return imc, categoria

# Función principal para ingresar datos del paciente
def main():
    print("Bienvenido al Centro Médico")
    
    # Lista para almacenar los datos de los pacientes
    pacientes = []
    
    for i in range(3):  # Solicitar datos de tres pacientes
        print(f"\nIngrese los datos del paciente #{i+1}")
        nombre = input("Nombre del paciente: ")
        peso = float(input("Peso en kg: "))
        altura = float(input("Altura en metros: "))
        
        # Calcular IMC y categoría utilizando la función
        imc, categoria = calcular_imc(peso, altura)
        
        # Almacenar los datos del paciente en una lista
        paciente = {
            "Nombre": nombre,
            "Peso": peso,
            "Altura": altura,
            "IMC": imc,
            "Categoría": categoria
        }
        
        pacientes.append(paciente)
    
    # Mostrar resultados para todos los pacientes
    print("\nResultados para los pacientes:")
    for paciente in pacientes:
        print(f"\nNombre: {paciente['Nombre']}")
        print(f"Peso: {paciente['Peso']} kg")
        print(f"Altura: {paciente['Altura']} m")
        print(f"IMC: {paciente['IMC']:.2f}")
        print(f"Categoría: {paciente['Categoría']}")

if __name__ == "__main__":
    main()