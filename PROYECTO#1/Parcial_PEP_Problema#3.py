filas = int(input("Ingrese el número de filas de la matriz: "))
columnas = int(input("Ingrese el número de columnas de la matriz: "))
#LA MATRIZ SE VA CREANDO
matriz = [[0 for j in range(columnas)] for i in range(filas)] #SE VA CREANDO LA MATRIZ CON FILAS Y COLUMNAS AL MISMO TIEMPO
contador = 1
for i in range(filas):
    if i % 2 == 0:
        for j in range(columnas):       #SI LA FILA ES PAR SE LLENA DE DERECHA A IZQUIERDA
            matriz[i][j] = contador
            contador += 1
    else:
        for j in range(columnas - 1, -1, -1):
            matriz[i][j] = contador             #SI LA FILA ES IMPAR SE LLENA DE IZQUIERDA A DERECHA
            contador += 1

print("La matriz llena en forma de zigzag es:")
for i in range(filas):
    print("[", end="")
    for j in range(columnas):
        print(matriz[i][j], end=" ")
    print("]")