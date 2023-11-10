# My proyect CRUD -> Generar, actualizar, eliminar, buscar

clients = 'Luis, Kevin'

def create_client(client_name):
    global clients
    if client_name not in clients: # when the client not found
        _add_comma()
        clients += client_name
        
    else:
        print("Client already exists {}:".format(client_name))

def _add_comma():
    global clients
    clients +=", "

def read_client():
    global clients
    print(clients)

def update_client(client_name, new_client):
    global clients
    if client_name in clients:
        clients = clients.replace(client_name+",",new_client+",")
    else:
        print("Client  is not in client list)")
        
def delete_client(cl_nn):
    global clients
    if cl_nn in clients:
        clients = clients.replace(cl_nn+",","")
    else:
        print('Client is not in client list')


def _print_welcome():
    print("WELCOME UNIVERSIDAD DEL VALLE -TULUÁ")
    print('*' * 100)
    print("What would you like to do today:")
    print("[C]reate Client o user:")
    print("[R]read Client o user:")
    print("[U]pdate Client o user:")
    print("[D]elete Client o user:")

def _get_client_name(): # la función me permite preguntar por el nombre del cliente
    return input("Type your name client: ")



if __name__ == '__main__':
    _print_welcome()
    option = input("Type option desired client:").upper()

    if option == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        read_client()

    elif option == 'R':
        read_client()

    elif option == 'U':
        client_name = _get_client_name()
        client_name_update = input("What is the update client Name:")
        update_client(client_name, client_name_update)
        read_client()
    
    elif option == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        read_client()
    else:
        print("command invalid")