# A comprehensive and useful dictionary of functions using sort_algorithms

'''
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. This algorithm is not efficient for large data sets as its average and worst-case time complexity are quite high.

- Sorts the array using multiple passes. After the first pass, the maximum goes to end (its correct position). 
  Same way, after second pass, the second largest goes to second last position and so on.
- In every pass, process only those that have already not moved to correct position. After k passes, the largest k must have been moved to the last k positions.
- In a pass, we consider remaining elements and compare all adjacent and swap if larger element is before a smaller element. If we keep doing this, we get the largest (among the remaining elements) at its correct position.
'''
def bubble_sort_1D_int_lists(arr: list[int]) -> None:
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                aux = arr[i]
                arr[i] = arr[j]
                arr[j] = aux

'''
Selection Sort is a comparison-based sorting algorithm. 
It sorts by repeatedly selecting the smallest (or largest) element from the unsorted portion and swapping it with the first unsorted element.

- Find the smallest element and swap it with the first element. This way we get the smallest element at its correct position.
- Then find the smallest among remaining elements (or second smallest) and swap it with the second element.
- We keep doing this until we get all elements moved to correct position.
'''
def selection_sort_1D_int_lists(arr:list[int]) -> None:
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        min_value = arr.pop(min_index)
        arr.insert(i, min_value)

'''
How Insertion Sort Works
- Start from the second element (as the first one is already considered sorted).
- Compare the current element (called key) with the elements before it.
- Shift all larger elements one position to the right.
- Insert the key into its correct position.
- Repeat until the entire array is sorted.
'''
def insertion_sort_1D_int_lists(arr: list[int]) -> None:
    arr_size = len(arr)-1
    if arr_size<1:
        return
    
    current_unsorted = 1

    while current_unsorted<=arr_size:
        # Consider that we have 2 arrays, one is sorted while the other is not
        # Here we move to the left sorted side of the list
        sorted = 0

        # In this loop we compare and we add the element to where it belongs
        while sorted<current_unsorted:
            if (arr[current_unsorted] <= arr[sorted]):
                change = arr.pop(current_unsorted)
                arr.insert(sorted, change)
            else:
                sorted += 1

        current_unsorted += 1