# A comprehensive and useful dictionary of functions using sort_algorithms

def bubble_sort_1D_int_lists(arr: list[int]) -> None:
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                aux = arr[i]
                arr[i] = arr[j]
                arr[j] = aux

def selection_sort_1D_int_lists(arr:list[int]) -> None:
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        min_value = arr.pop(min_index)
        arr.insert(i, min_value)
