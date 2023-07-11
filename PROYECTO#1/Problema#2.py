#Luzmar Almao  C.I: 27296990
#Manuel Planas C.I: 27373001
H = float(input("Ingrese la profundidad del pozo en metros: "))
Ld = float(input("Ingrese la distancia que el caracol sube durante el día en metros: "))
Ln = float(input("Ingrese la distancia que el caracol desciende durante la noche en metros: "))

dias = 0
distancia = 0

if Ln <= Ld:
    while distancia < H:
        dias += 1
        distancia += Ld
        distancia -= Ln
    print("El caracol sale del pozo en", dias, "días.")
else:
    print("El caracol no pudo salir del pozo")