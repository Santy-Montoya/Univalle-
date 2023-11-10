# Dictionary

dic = {"Animal":"Gato", "Cosa":"Piedra", "Lenguaje_p":"Java"}
#print(dic)

#Aceder a los elementos de un dicionario

#print(dic["Animal"], dic["Lenguaje_p"])


def run():
    for llave in dict.keys():
        print(llave)

    for valor in dict.values():
        print(valor)

    for llave, valor in dict.items():
        print("La llave:"+ llave +" , " + " Su valor es:"+ valor)


if __name__ == "__main__":
    run()