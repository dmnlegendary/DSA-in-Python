# Aprender sobre uso de listas en python
# La declaracion de listas se hace entre square brackets []
import random
import sort_algorithms as sort

lista_numeros_enteros: list[int] = [1,2,3,4,5]
print(lista_numeros_enteros, end="\n\n") # Imprime el contenido de la lista completa

for valor in lista_numeros_enteros: # itera con la variable valor en cada elemento de la lista
    print(valor) # imprime de uno en uno cada valor
print()

for i in range(len(lista_numeros_enteros)): # Itera por un ciclo que no entra en la lista, mas bien en su tamaño
    print(f"Posicion {i}: [{lista_numeros_enteros[i]}]")
print()

# Añadir elemento
lista_numeros_enteros = lista_numeros_enteros + [10] + [20]
print(lista_numeros_enteros)

print(lista_numeros_enteros[::2]) # recorrer lista usando el formato inicio:final:incremento

list_with_random_int = [random.randint(1,100) for _ in range(random.randint(10,100))]
print("random numbers generated are:")
print(list_with_random_int)

# Using several sort algorithms here
# sort.bubble_sort_1D_int_lists(list_with_random_int)
sort.selection_sort_1D_int_lists(list_with_random_int)
print("random numbers generated BUT SORTED are:")
print(list_with_random_int)
'''
*****METHODS USED IN ARRAYS*****
arr.append(element) # adds an element at the end of the list
arr.clear() # removes all elements in list
new_arr = arr.copy() # copies all elements in list

times_appear = arr.count(element) # returns the number of times '9' appears in the list
points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9) # returns the number of times '9' appears in the list

arr.extend(iterable) # adds at the end of the list either an element or another list, tuple, set or any iterable
fruits = ['apple', 'banana', 'cherry']
points = (1, 4, 5, 9)
fruits.extend(points)

where_is_index = list.index(elmnt, start, end) # search a certain element within the list from a start position to an end position

arr.insert(position, element) # adds an element in an specific position

list.pop(pos) # Removes the element in an specific position

list.remove(elment) # removes the first occurrence of the element with the specified value.

list.reverse() # reverses the sorting order of the elements.

list.sort(reverse=True|False, key=myFunc) # The sort() method sorts the list ascending by default.
'''
def test_using_while() -> None:
    times_reaching_number_5 = 0
    index = 0
    
    # The while loop gives you complete control over 'index'
    while index < 10:
        # We use < 3 so it resets exactly 3 times
        if index == 5 and times_reaching_number_5 < 3:
            times_reaching_number_5 += 1
            print(f"We have reached 5 for the {times_reaching_number_5} time")
            
            # Manually reset the index back to 0
            index = 0
        else:
            print(f"Position {index}")
            
            # Manually advance the index
            index += 1

print(
    "\nHagamos un nuevo ejercicio.\nSe creara un arreglo de 0s y 1s aleatorio, con un tamano desde 1 hasta 1000.\n" \
    "El arreglo se ordenara dejando los 1s de un lado y los 0s del otro, no importa en que extremo queden.\n" \
    "Tambien se contabilizara la cantidad de cambios adyacentes que se hagan.\n" \
    "Los cambios solo se pueden hacer a la izquiera o derecha por numero."
    )

'''
Lets imagine a list like [1,0,1,0,1,0,1,0]
-> [1,0,1,0,1,0,1,0] i=1
-> [1,0,1,0,1,0,1,0]
-> [1,1,0,0,1,0,1,0]
-> [1,1,0,0,1,0,1,0]
'''
def swap_numbers(arr: list[int]) -> int:
    size_arr = len(arr)
    left_end = arr[0]

    current = 1
    swapped_numbers = 0
    while (current <= (size_arr-1)):
        if (arr[current]!=arr[current-1]) and (left_end==arr[current]):
            '''
            change = arr.pop(current)
            arr.insert(current-1, change)
            current = current - 1
            change = None
            swapped_numbers += 1
            '''
            aux = arr[current]
            arr[current] = arr[current-1]
            arr[current-1] = aux
            swapped_numbers += 1
            current = current - 1
            continue

        current += 1

    return swapped_numbers

# lista_binaria = [random.randint(0,1) for _ in range(random.randint(1,1000))]
lista_binaria = [1,0,1,0,1,0,1,0]
print("La lista generada es:")
print(lista_binaria)

veces_cambiado = swap_numbers(lista_binaria)
print(f"Se hicieron un total de {veces_cambiado} cambios adjuntos para acomodar la lista\nLa lista quedo de esta forma:")
print(lista_binaria)