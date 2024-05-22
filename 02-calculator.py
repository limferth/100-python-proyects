def suma (a, b):
    return a + b

def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b 

def division(a, b):
    return a / b

#preguntar al usuario la operacion que quiere realizar
while True:
    try:
        operacion = int(input("seleccione la operacion que desea realizar: "
            "\n1. Suma\n2. Resta\n3. Multiplicacion\n4. Division\n"))
        (operacion <= 4 and operacion >= 0)
        break
    except:
        print("ingrese un valor valido")


#Pedir al usuario los numeros a operar
num1 = float(input("ingrese el primer numero: "))
num2 = float(input("ingrese el segundo  numero: "))

if operacion == 1:
    resultado = suma(num1, num2)
elif operacion == 2:
    resultado = resta(num1, num2)
elif operacion == 3:
    resultado = multiplicacion(num1, num2)
elif operacion == 4:
    resultado = division(num1, num2)
else:
    resultado = "sintax error"
    print("sintax error")

print(f"Resultado:  {resultado}")