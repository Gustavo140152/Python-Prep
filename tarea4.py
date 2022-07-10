# 1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla

ciudades = ['Bogotá D. C.','Paris', 'Madrid', 'Quito', 'Lima', 'Frankfurt', 'Lisboa', 'Sidney']
print(ciudades)

# 2) Imprimir por pantalla el segundo elemento de la lista

print (ciudades[1])

# 3) Imprimir por pantalla del segundo al cuarto elemento

print (ciudades[1:4])

# 4) Visualizar el tipo de dato de la lista

print (type(ciudades))

# 5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento

print(ciudades[2:])

# 6) Visualizar los primeros 4 elementos de la lista

print(ciudades[:4])

# 7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?

ciudades.append('Madrid')
ciudades.append('Sao Pablo')
print (ciudades)

# 8) Agregar otra ciudad, pero en la cuarta posición

ciudades.insert(3, 'Mexico DF')
print (ciudades)

# 9) Concatenar otra lista a la ya creada

ciudades.extend(['La Paz', 'Santiago De Chile', 'Buenos Aires'])
print (ciudades)

# 10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?

print (ciudades.index('Madrid')) # si el item es repetido mostrará el indice del primer elemento encontradop

# 11) ¿Qué pasa si se busca un elemento que no existe?

# print(ciudades('Tunja'))

# 12) Eliminar un elemento de la lista

ciudades.remove('Madrid') # si el item es repetido eliminará el primero que encuentre
print(ciudades)

# 13) ¿Qué pasa si el elemento a eliminar no existe?

print('Si el elemento a eliminar no exixte mostrara un mensaje de un error')

# 14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo

ultitem = ciudades.pop()
print (ultitem)

# 15) Mostrar la lista multiplicada por 4

print(ciudades*4)

# 16) Crear una tupla que contenga los números enteros del 1 al 20

tup1_20 = []
for n in range (0,20):
    tup1_20.append(n+1)
tupla1_20 = tuple(tup1_20)
print (tupla1_20)

# 17) Imprimir desde el índice 10 al 15 de la tupla

print(tupla1_20[9:15])

# 18) Evaluar si los números 20 y 30 están dentro de la tupla

if 20 in tupla1_20:
    print (20, True)
else:
    print (20, False)
if 30 in tupla1_20:
    print (30, True)
else:
    print (30, False)

# 19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.

city = 'Paris'
if city in ciudades:
    print (city, 'ya existe')
else:
    ciudades.append(city)
    print (ciudades, 'se inserto, ', city, 'al final')

# 20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista

cities = ['Bogotá D. C.','Paris', 'Madrid', 'Quito', 'Lima', 'Frankfurt', 'Madrid', 'Madrid']
cities = tuple(cities)
rep_tupla = cities.count('Madrid')
print ('Madrid esta repetido', rep_tupla, ' veces el la tupla cities')
rep_lista = ciudades.count('Bogotá D. C.')
print ('Bogotá D. C. se encuenta', rep_lista, ' veces en la lista ciudades')

# 21) Convertir la tupla en una lista

ciutuplalist = list(cities)
ciutuplalist.append('Tunja')
print (ciutuplalist)

# 22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables

