# Necesitaremos usar numpy para hacer mas manipulables las matrices en python
# Veremos las formas de hacerlo con y sin numpy

import numpy as np
import random

random.seed()

# el usuario ingresa la cantidad de filas y columnas que desea:
filas = int(input("Ingresa filas: "))
columnas = int(input("Ingresa columnas: "))

# de esta forma inicializamos toda la matriz con zeros
matriz_de_zero = [[random.randint(1, filas+columnas) for value1 in range(columnas)] for value2 in range(filas)]

for i in range(len(matriz_de_zero)):
    for j in range(len(matriz_de_zero[0])):
        print(f"Pos [{i},{j}] = {matriz_de_zero[i][j]}", end=", ")
    print()

# Ejemplo de obtener las dimensiones de una matriz
matrix_dimension = [
    [1, 2, 3],
    [4, 5, 6]
]
ROWS = len(matrix_dimension)
COLS = len(matrix_dimension[0]) if ROWS > 0 else 0
print(matrix_dimension)
print(f"Dimensiones de la matriz anterior es: ({ROWS}, {COLS})")

# Vamos a hacer un ejemplo:
# Dado una lista de numeros enteros: [4,4,4,3,3,2,9,1,3,5,7,0]
# Crear en otra lista el registro de frecuencia en orden descendente con base al valor numerico de cada numero
# Es decir el arreglo superior deberia ser leido como: [[9,1], [7,1], [5,1], [4,3], [3,3], [2,1], [1,1], [0,1]]

def ordenar_frecuencias(arr: list[int]):
    # Esta lista (matriz) devuelve los resultados
    arr_ordenado = []

    # Primero ordenamos los elementos de la lista
    # Las listas son mutables por lo que haremos una copia
    test_arr = arr.copy()
    # la ordenamos
    test_arr.sort()
    # la volteamos para agilidad
    test_arr.reverse()

    # En este arreglo buscaremos los numeros unicos dentro del arreglo
    numeros_a_analizar = []
    for index in range(len(test_arr)):
        if test_arr[index]!=test_arr[index-1] or len(test_arr)<1:
            numeros_a_analizar.append(test_arr[index])
    print("\nNumeros organizados de mayor a menor y sin repetir:")
    print(numeros_a_analizar)

    # En esta seccion buscaremos las frecuencias de todos
    for analyzed_pos in range(len(numeros_a_analizar)):
        frequency = 0
        for comparing_pos in range(len(test_arr)):
            if numeros_a_analizar[analyzed_pos] == test_arr[comparing_pos]:
                frequency += 1
            else:
                continue
        arr_ordenado.append([numeros_a_analizar[analyzed_pos], frequency])

    return arr_ordenado

lista_numeros: list[int] = [random.randint(0,10) for _ in range(random.randint(1,100))]
print("\nSe han generado los siguientes numeros:")
print(lista_numeros)

lista_calculada = ordenar_frecuencias(lista_numeros)
print("\nEstas son las frecuencias de los numeros:")
print(lista_calculada)