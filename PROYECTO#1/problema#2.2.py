#Luzmar Almao  C.I: 27296990
#Manuel Planas C.I: 27373001
H = float(input("Ingrese la profundidad del pozo en metros: "))
Ld = float(input("Ingrese la distancia que el caracol sube durante el día en metros: "))
Ln = float(input("Ingrese la distancia que el caracol desciende durante la noche en metros: "))

if Ld>=H:
    print("El caracol salió del pozo el mismo día.")
elif Ld <= Ln:
    print("El caracol no pudo salir del pozo.")
else:
    distancia=0
    dias=0
    while distancia < H:
        dias += 1
        distancia += Ld
        distancia -= Ln
    print("El caracol sale del pozo en", dias, "días.")
