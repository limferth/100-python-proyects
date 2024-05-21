#proyect easy
import string
import random

def generar_cantrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ""
    for i in range(longitud):
        contrasena += random.choice(caracteres)
        print(contrasena)
    return contrasena

longitud = int(input("Cual es la longitud de la contrasena deseada:  "))
nueva_contrasena = generar_cantrasena(longitud)
print("la nueva contrasena es: ", nueva_contrasena)