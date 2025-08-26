def bubble_sort(matrix):
    """Sorts the first row using Bubble Sort. Returns the sorted first row list and the number of swaps performed."""
    row = matrix[0]
    n = len(row)
    swaps = 0
    for i in range(n):
        for j in range(n - 1 - i):
            if row[j] > row[j + 1]:
                row[j], row[j + 1] = row[j + 1], row[j]
                swaps += 1
    return row, swaps

def insertion_sort(matrix):
    """Sorts the second row using Insertion Sort. Returns the sorted second row list and the number of swaps performed."""
    row = matrix[1]
    n = len(row)
    swaps = 0
    for i in range(1, n):
        key = row[i]
        j = i - 1
        while j >= 0 and row[j] > key:
            row[j + 1] = row[j]
            j -= 1
            swaps += 1
        row[j + 1] = key
    return row, swaps

def selection_sort(matrix):
    """Sorts the third row using Selection Sort. Returns the sorted third row list and the number of swaps performed."""
    row = matrix[2]
    n = len(row)
    swaps = 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if row[j] < row[min_idx]:
                min_idx = j
        if min_idx != i:
            row[i], row[min_idx] = row[min_idx], row[i]
            swaps += 1
    return row, swaps

def merge(first_row, second_row, third_row):
    """
    Merges three sorted rows of the matrix into one sorted 1D list.
    
    Args:
        matrix (list of list of int): 2D list (matrix) where each row has 'n' elements and is sorted.
    
    Returns:
        list: A merged 1D list that contains all elements from the matrix in sorted order.
    """
    sorted_list = []
    i = j = k = 0
    n = len(first_row)  # Since each row has the same number of elements
    
    while i < n or j < n or k < n:
        # Compare elements in each row, making sure to stay within bounds
        smallest = float('inf')
        target_row = 0

        if i < n and first_row[i] < smallest:
            smallest = first_row[i]
            target_row = 1
        if j < n and second_row[j] < smallest:
            smallest = second_row[j]
            target_row= 2
        if k < n and third_row[k] < smallest:
            smallest = third_row[k]
            target_row = 3

        # Add the smallest element to the merged list and move the corresponding index forward
        if target_row == 1: 
            sorted_list.append(first_row[i])
            i += 1
        elif target_row == 2:
            sorted_list.append(second_row[j])
            j += 1
        elif target_row == 3:
            sorted_list.append(third_row[k])
            k += 1

    return sorted_list
