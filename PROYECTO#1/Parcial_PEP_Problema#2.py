H = float(input("Ingrese la profundidad del pozo en metros: "))
Ld = float(input("Ingrese la distancia que el caracol sube durante el día en metros: "))
Ln = float(input("Ingrese la distancia que el caracol desciende durante la noche en metros: "))

dias = 0
distancia = 0
iteracion=0
while distancia < H and iteracion<500:
    dias += 1
    distancia += Ld
    distancia -= Ln
    iteracion+=1
    if iteracion == 99 and distancia < H:
        print("El caracol no logró salir del pozo.")
        break
if distancia >= H:
    print("El caracol sale del pozo en", dias, "días.")