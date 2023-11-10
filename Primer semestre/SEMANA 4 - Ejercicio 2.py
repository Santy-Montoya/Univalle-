#funciones 

def  message(): #se genera una funcion llamada message
    print("Hello word")

#def suma (a,b):
    #total = a + b
    #print("la suma total es: {}". format (total))
def suma (a,b):
    total = a + b
    return total 
    #print("la suma total es: {}". format (total))

#entry point for inicializations our programs
if __name__ == '__main__' :
    # #message()  #se invoca la funcion 
    # suma(1,2)
    # x = suma(1,2)
    # print ("the value of suma is {}". format(x))

    a = int(input("Enter a number one:"))
    b = int(input("Enter a number two:"))
    x = suma(a,b)
    print ("the value of suma is {}". format(x))
    ________________
def dame_pi():
    num_pi = 3.14159
    return num_pi
_________
devolver = dame_pi()
    print(devolver)