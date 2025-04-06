n = int(input("Ingrese un número entero positivo (1 a 9) que desee elevar: "))

if n <= 0 or n > 9:
    print("El número debe estar entre 1 y 9.")
else:
    x = 0
    while x <= n:
        resultado = n ** x
        print(f"{n}^{x} = {resultado}")
        x += 1