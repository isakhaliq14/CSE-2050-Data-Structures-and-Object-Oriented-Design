import math
from enum import Enum

INVERSION_BOUND = 10  # pre-defined constant; independent of list input sizes

class MagicCase(Enum):
    """Enumeration for tracking which case we want to use in magicsort"""
    GENERAL = 0
    SORTED = 1
    CONSTANT_INVERSIONS = 2
    REVERSE_SORTED = 3

def linear_scan(L):
    inversions = sum(1 for i in range(len(L) - 1) if L[i] > L[i + 1])
    if inversions == 0:
        return MagicCase.SORTED
    if inversions == len(L) - 1:
        return MagicCase.REVERSE_SORTED
    if inversions <= INVERSION_BOUND:
        return MagicCase.CONSTANT_INVERSIONS
    return MagicCase.GENERAL

def reverse_list(L, alg_set=None):
    if alg_set is not None:
        alg_set.add("reverse_list")
    L.reverse()

def magic_insertionsort(L, left, right, alg_set=None):
    if alg_set is not None:
        alg_set.add("magic_insertionsort")
    for i in range(left + 1, right):
        key = L[i]
        j = i - 1
        while j >= left and L[j] > key:
            L[j + 1] = L[j]
            j -= 1
        L[j + 1] = key

def magic_mergesort(L, left, right, alg_set=None):
    if right - left <= 20:
        magic_insertionsort(L, left, right, alg_set)
        return
    if alg_set is not None:
        alg_set.add("magic_mergesort")
    mid = (left + right) // 2
    magic_mergesort(L, left, mid, alg_set)
    magic_mergesort(L, mid, right, alg_set)
    
    temp = []
    i, j = left, mid
    while i < mid and j < right:
        if L[i] <= L[j]:
            temp.append(L[i])
            i += 1
        else:
            temp.append(L[j])
            j += 1
    temp.extend(L[i:mid])
    temp.extend(L[j:right])
    L[left:right] = temp

def magic_quicksort(L, left, right, depth=0, alg_set=None):
    if right - left <= 20:
        magic_insertionsort(L, left, right, alg_set)
        return
    
    if depth > 3 * math.log2(len(L) + 1):
        magic_mergesort(L, left, right, alg_set)
        return
    
    if alg_set is not None:
        alg_set.add("magic_quicksort")
    
    pivot = L[right - 1]
    i = left
    for j in range(left, right - 1):
        if L[j] < pivot:
            L[i], L[j] = L[j], L[i]
            i += 1
    L[i], L[right - 1] = L[right - 1], L[i]
    
    magic_quicksort(L, left, i, depth + 1, alg_set)
    magic_quicksort(L, i + 1, right, depth + 1, alg_set)

def magicsort(L):
    alg_set = set()
    case = linear_scan(L)
    
    if case == MagicCase.SORTED:
        return alg_set
    elif case == MagicCase.REVERSE_SORTED:
        reverse_list(L, alg_set)
    elif case == MagicCase.CONSTANT_INVERSIONS:
        magic_insertionsort(L, 0, len(L), alg_set)
    else:
        magic_quicksort(L, 0, len(L), 0, alg_set)
    
    return alg_set