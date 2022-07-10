## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

from multiprocessing.sharedctypes import Value


a=-80
if(a > 0):
    print ('El elemento es mayor a cero')
else:
    print ('El elemento es menor a cero')    
# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

a= 25
b='perros'
if (type(a) == type(b)):
    print ('son del mismo tipo de dato y son ', type(a))
else:
    print(a, ' es del tipo ', type(a), ' y b es del tipo ', type(b))

# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

for i in range (1,21):
    if (i % 2 == 0):
        print (i, ' es par')
    else:
        print (i, ' es impar')

# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia iguala 3

for n in range(0,6):
    print (n, 'elevado a 3 es igual a', n**3)

# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

a = 5

for i in range(1,a+1):
    print ('ciclo ',i)

# 6) Utilizar un ciclo while para realizar el factorial de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

y = 5
ini = y
fact = 1
while (ini > 1):
    fact = fact * ini
    ini = ini -1
print (y, 'factorial es igual a ', fact)

x = 10
if (x > 0):        
    fact = 1
    inicial = x
    for inicial in range (2, inicial+1):
        fact = fact * inicial
    print ('El factorial de ', x, ' es igual a ', fact)
else:
    print ('no se puede calcular el factorial de ', x)

# 7) Crear un ciclo for dentro de un ciclo while

# 8) Crear un ciclo while dentro de un ciclo for

# 9) Imprimir los números primos existentes entre 0 y 30

n = 30
for i in range (2,n):
    if i == 2:
        print (i, 'es primo')
        continue
    elif i % 2 == 0:
        continue
    else:
        for k in range(2, i):
            if (i % k == 0):
                break
        else:
            print(i, 'primo')
        
# 13) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

x = 99
while (x <= 300):
    x = x + 1
    if x % 12 == 0:
        print (x, ' y número dividudo 12 es igual a ',x / 12)

# 14) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

n = 1
sigue = 1
primo = True
while (sigue == 1):
    for div in range(2, n):
        if (n % div == 0):
            primo = False
            break
    if (primo):
        print(n)
        print('¿Desea encontrar el siguiente número primo?')
        if (input() != '1'):
            print('Se finaliza el proceso')
            break
    else:
        primo = True
    n += 1

x = int(input ('si desea crear un número primo presione un número NATURAL de lo contrario presione 0'))
if x == 0:
    print ('usted selecciono 0')
else:
    for div in range (2, x):
        if x % div == 0:
            break
    else: print (x, 'es primo)')
    print (x,' no es un número primo')
    print ('encontrar el siguiente número primo')
    

