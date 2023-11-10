def mayor_pedido(municipio):
    mayor = 0
    total = 0
    for i in range(5):
        pedido = int(input(f"Ingrese la cantidad de productos pedidos en el punto {i+1}: "))
        if pedido > mayor:
            mayor = pedido
            punto = i+1
        total += pedido
    print(f"El total de productos pedidos en el municipio de {municipio} es {total}")
    print(f"El punto de entrega con mayor pedido en el municipio de {municipio} es el punto {punto}")

municipio1 = input("Ingrese el nombre del primer municipio: ")
mayor_pedido(municipio1)

municipio2 = input("Ingrese el nombre del segundo municipio: ")
mayor_pedido(municipio2)

municipio3 = input("Ingrese el nombre del tercer municipio: ")
mayor_pedido(municipio3)