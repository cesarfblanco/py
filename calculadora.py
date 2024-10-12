def sumar(a,b):
    return a + b

def restar(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    if b == 0:
        return "No se puede dividir por cero"
    return a / b

print("Selecciona operación:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = input("Elige una opcion (1/2/3/4): ")

num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el segundo numero: "))

if opcion == "1":
    print(f"Resultado: {sumar(num1,num2):.0f}")
elif opcion == "2":
    print(f"Resultado: {restar(num1, num2):.0f}")
elif opcion == "3":
    print(f"Resultado: {multiplicar(num1, num2):.0f}")
elif opcion == "4":
    print(f"Resultado: {dividir(num1, num2):.0f}")
else:
    print("opcion no valida")