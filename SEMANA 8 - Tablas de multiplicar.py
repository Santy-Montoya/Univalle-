
# for i in range(1, 11):
#     print (f"Multiplication table of {i}:")
# for j in range (1, 11):
#     print(f"{i} × {j} = {i*j}")
# print()



for i in range(1, 11):
    valor = int(input("Ingrese un numero: "))
    for j in range(1, 11):
        if i * j == valor:
            print (f"{i} X {j}")
    print(0)

  