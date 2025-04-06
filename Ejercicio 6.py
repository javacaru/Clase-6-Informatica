op=1
while op==1:
    n = int(input("Ingrese el número de veces que quiere realizar la sumatoria (n): "))
    a = float(input("Ingrese el valor que desea para su denominador a (≠ 0): "))
    if a == 0:
        print("Error: El valor de 'a' no puede ser cero.")
    else:
        suma = 0
        i = 1
        while i <= n:
            termino = (1 / a) ** i
            suma += termino
            i += 1
            print(f"La suma es: {suma}")
    
    op=int(input("Desea continuar con el programa?\n 1-si \n 2-no "))
if op==2:
    print("Fin del programa")                

