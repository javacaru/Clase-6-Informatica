cantidadnotas = int(input("Cuantas notas deseas ingresar"))

contador = 0
suma = 0

while contador < cantidadnotas:
    print(f"Ingrese la nota #{contador + 1} (de 0 a 5):")
    nota = float(input())

    if nota < 0 or nota > 5:
        print("La nota debe estar entre 0 y 5. Intenta de nuevo.")
        continue  # vuelve a pedir la misma nota
    suma = suma + nota
    contador = contador + 1

promedio = suma / cantidadnotas
print(f"El promedio final es: {round(promedio,2)}")
