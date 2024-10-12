import random

adivinaNumero = int(random.randint(1,20))
adivina = False
intentos = 0

print("Estoy pensando en un numero del 1 al 20")

while not adivina:
    numUser= int(input("Adivina el numero: "))
    intentos+=1

    if numUser>adivinaNumero:
        print("El numero es menor")
    elif numUser<adivinaNumero:
        print("El numero es mayor")
    else:
        adivina = True
        print(f"Correcto, adivinaste el numero en: {intentos} intentos")



