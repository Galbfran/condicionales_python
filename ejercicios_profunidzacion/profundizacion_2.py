# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite el ingreso de tres números
enteros, y luego en cada caso informe si el número es par
o impar.
Para cada caso imprimir el resultado en pantalla.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

def par_impar():
    for numero in range(cantidad_numeros):
        numero = int(input("Ingrese numero."))
        if (numero%2) == 0:
            print("El numero {} es par.".format(numero))
        else:
            print("El numero {} es impar.".format(numero))


if __name__ == '__main__':
    cantidad_numeros = int(input("Ingrese la cantidad de numeros a consultar.\n"))

    par_impar()