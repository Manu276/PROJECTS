##NUMEROS ALEATORIOS 2.0

N = input("Ingrese un valor semilla de 4 cifras numericas: ")

intentos = 0
while intentos <= 3 :
    #se confirma que el valor ingresado sea un numero y que su longitud sea de 4 cifras
    if N.isnumeric() and len(N) == 4:
        #se convierte el valor ingresado a un numero entero
        N = int(N)
    
        veces = input("Ingrece la cantidad de veces que quiere repetir el proceso: ")
        veces_int = int(veces)
        #ciclo for para realizar las operaciones tantas veces quiera el usuario
        for i in range(0, veces_int) :
            N_cuadrado = N**2
            
            N_cadena = str(N_cuadrado)
            N_medio = int(N_cadena[2:6])
            N_medio_int = str(N_medio)
            N_ceros = len(str(N_medio_int))
            N_ceros_cant = "1" + "0" * N_ceros
            N_ceros_cant = int(N_ceros_cant)
            N_aleatorio = N_medio/N_ceros_cant
            print(" El numero es: ", N, " Elevado al cuadrado es: ", N_cuadrado, " El numero aleatorio es: ", N_aleatorio)
            N = N_medio
    
        break

    else :    

        print("***EL VALOR SEMILLA INGRESADO NO ES VALIDO***")
        intentos += 1 
        intentos_1 = 4 - intentos
        print("le quedan ", intentos_1, "intentos" )
        N = input("ingrese un valor semilla valido: ") 

if intentos == 4 :
    print("Alcanzo el numero maximo de intentos. bai")

