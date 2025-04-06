N = int(input("Ingrese un número entero positivo (N ≥ 1): "))

if N < 1:
    print("N debe ser mayor o igual a 1.")
else:
    suma = 0
    i = 1
    while i <= N:
        suma += i
        i += 2
    print(f"La suma de los números impares entre 1 y {N} es: {suma}")
