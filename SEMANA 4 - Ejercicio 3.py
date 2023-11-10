#functions numer two 

def  identification(name, gender):
    print ("Hi:{}". format(name))
    if gender == "M":
        print("confirmado, eres genero Masculino")
    elif gender == "F":
        print("confirmado, eres genero Mujer ")
    elif gender == "NB":
        print("confirmado, eres genero Mujer ")
    else:
        print("no compartirlo...")

if  __name__ == '__main__':
    name = input("emter your name:").upper ()
    gender = input ("enter your gender:").upper()
    identification (name, gender,)