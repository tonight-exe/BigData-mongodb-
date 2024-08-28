#lanza la app y cunfiona como interface de usuario
from funcions import *
def main ():
    while True:
        try:
            opcion = int(input("1 para llenar/n2 para ver /n3 para salir"))
            while opcion < 1 or opcion >4:
                print("error")
                opcion = int(input("1 para llenar/n2 para ver /n3 para salir"))
        except:
            print("error")
        if opcion == 1:
            ingresa()
            if opcion == 2:
                muestra_datos_rut()
            if opcion == 3:
                break
main()                        


    