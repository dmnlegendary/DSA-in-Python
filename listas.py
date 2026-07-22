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