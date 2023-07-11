Luzmar Almao  C.I: 27296990
Manuel Planas C.I: 27373001
#EMPLEADO

productos_disponibles = []

while True:
    nombre = input("Ingrese el nombre del producto (o 'salir' para terminar): ")
    nombre = nombre.lower()
    if nombre == 'salir':
        break

    while True:
        if nombre.isalpha():
            break
        else:
            print("Error: Ingrese solo letras para el nombre del producto.")
            nombre = input("Ingrese el nombre del producto: ")

    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad de productos: "))
            break
        except ValueError:
            print("Error: Ingrese un valor numérico para el precio y la cantidad.")

    productos_disponibles.append({'nombre': nombre, 'precio': precio, 'cantidad': cantidad})

print(" ")
print(" ")
print("###########################################")
print("##########  Lista de productos:  ##########")
print("###########################################")
print(" ")
print(" ")


for producto in productos_disponibles:
  
  print("{} - ${} - {} unidades".format(producto['nombre'], producto['precio'], producto['cantidad']))

##La función format() toma los valores que se van a insertar en la cadena y los coloca en los lugares correspondientes dentro de la cadena.

#CLIENTE
print(" ")
print(" ")
print("###################################################################")
print("##########  ESTIMADO CLIENTE INGRESE LA ORDEN DE COMPRA  ##########")
print("###################################################################")
print(" ")
print(" ")

productos_vendidos = []

while True:
  nombre = input("Ingrese el nombre del producto que desea (o 'salir' para terminar): ")
  nombre = nombre.lower()
  if nombre == 'salir':
    break

  while True :
    if nombre.isalpha():
      break
    else:
      print("Error: Ingrese solo letras para el nombre del producto.")
      nombre = input("Ingrese el nombre del producto que desea: ")
##
  for producto in productos_disponibles:
    if producto['nombre'] == nombre:
      while True:
        try:
          cantidad = int(input("ingrese la cantidad de productos que desea: "))
          if cantidad <= producto['cantidad']:
            break
          else:
            print("Disculpe, NO hay suficientes productos disponibles")
        except ValueError:
          print("Error: Ingrese un valor numerico para la cantidad de productos que desaea")

      productos_vendidos.append({'nombre': nombre, 'precio': producto['precio'], 'cantidad': cantidad})
      producto['cantidad'] -= cantidad
      break

  else:
    print("Los lamentamos el producto que desea no esta disponible")

print(" ")
print(" ")
print("###############################################################")
print("##########  La lista de los productos que desea es:  ##########")
print("###############################################################")
print(" ")
print(" ")

for producto in productos_vendidos:
  print("{} - ${} - {} unidades".format(producto['nombre'], producto['precio'], producto['cantidad']))


total = 0

print(" ")
print(" ")
print("############################################################")
print("##########  AQUI TE MUESTRO LA FACTURA DETALLADA  ##########")
print("############################################################")
print(" ")
print(" ")
for producto in productos_vendidos:
  subtotal = producto['precio'] * producto['cantidad']
  total += subtotal
  print("{} - ${} - {} unidades - ${} subtotal".format(producto['nombre'], producto['precio'], producto['cantidad'], subtotal))



print(" ")
print(" ")
print("####################################")
print("##########  EL TOTAL ES:  ##########")
print("####################################")
print(" ")
print(" ")

print("Total: ${}".format(total))
