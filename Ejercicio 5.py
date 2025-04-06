opcion = 1

while opcion == 1:
    numero = int(input("Ingrese un número entre 0 y 20: "))

    if numero < 0 or numero > 20:
        print("Número inválido. Debe estar entre 0 y 20.")
    else:
        factorial = 1
        i = 1
        while i <= numero:
            factorial *= i
            i += 1
        print(f"El factorial de {numero} es: {factorial}")

    print("\n¿Desea intentar de nuevo?")
    opcion = int(input("Seleccione una opción \n 1-si \n 2-No  "))
if opcion==2:
    print("Fin del programa")  
