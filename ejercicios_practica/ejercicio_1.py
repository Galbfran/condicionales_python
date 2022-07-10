# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica

# Comparadores
# Ingrese dos números cualesquiera y realice las sigueintes
# comparaciones entre ellos
numero_1 = int(input('Ingrese el primer número:\n'))

numero_2 = int(input('Ingrese el segundo número:\n'))

# Compare cual de los dos números es mayor
# Imprima en pantalla según corresponda
if numero_1 > numero_2:
    print("El primer numero:", numero_1 , "es mayor al segundo numero:", numero_2 )
elif numero_1 == numero_2:
    print("El primer numero:" , numero_1 , "es igual al segundo numero:", numero_2 )
elif numero_1 < numero_2:
    print("El segundo numero:" , numero_1 , "es mayor al primero numero:", numero_2 )
else:
    print("no se encuentro ningún rango válido")
# Verifique si el numero_1 positivo, negativo o cero
# Imprima el resultado en cada caso
if numero_1 == 0:
    print("El numero es 0.")
elif numero_1 < 0:
    print("El numero es 0.")
elif numero_1 > 0:
    print("El numero es mayor a 0.")
else:
    print("no se encuentro ningún rango válido")

# Verifique si el numero_1 es mayor a 0 y menor a 100
# Imprima en pantalla si se cumple o no la condición
if numero_1 >= 0 or numero_1 <= 100:
    print("El numero cumple el rango.")
elif numero_1 < 0 or numero_1 > 100:
    print("El numero no cumple con el rango")
# Verifique si el numero_1 es menor a 10 o el numero_2
# es mayor a -2
# Imprima en pantalla si se cumple o no la condición
if numero_1 < 10 and numero_2 >= -2:
    print("El primer numero es menor a 10 y el segundo numero mayor a -2.")
elif numero_1 >= 10 and numero_2 <= -2:
    print("El primer numero es mayor o igual a 10 y el segundo numero menor o igual a -2.")