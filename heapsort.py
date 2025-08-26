def idx_left(L, idx, right):
    """Return index of left child or None if out of range."""
    left = 2 * idx + 1
    return left if left < right else None

def idx_right(L, idx, right):
    """Return index of right child or None if out of range."""
    right_idx = 2 * idx + 2
    return right_idx if right_idx < right else None

def idx_max_child(L, idx, right):
    """Return index of max child or None if no children."""
    left = idx_left(L, idx, right)
    right_ = idx_right(L, idx, right)
    if left is None:
        return None
    if right_ is None:
        return left
    return left if L[left] > L[right_] else right_
    
def swap(L, i, j):
    """Swap values at index i and j."""
    L[i], L[j] = L[j], L[i]
    
def downheap(L, idx, right):
    """Restore max-heap from index to right."""
    child = idx_max_child(L, idx, right)
    while child is not None and L[child] > L[idx]:
        swap(L, idx, child)
        idx = child
        child = idx_max_child(L, idx, right)

def heapsort(L):
    """Sort the list in ascending order using heapsort."""
    n = len(L)
    for i in reversed(range(n // 2)):
        downheap(L, i, n)
    for end in reversed(range(1, n)):
        swap(L, 0, end)
        downheap(L, 0, end)
