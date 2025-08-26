from entry import Entry

class Heap:
    def __init__(self):
        """Create an empty heap."""
        self._L = []
        self._idx = {}

    def __len__(self):
        """Return number of items in heap."""
        return len(self._L)

    def __iter__(self):
        """Yield entries in order by priority (removes them)."""
        while self._L:
            yield self.remove_min()

    def idx_parent(self, idx):
        """Return index of parent or None if root."""
        return (idx - 1) // 2 if idx > 0 else None

    def idx_left(self, idx):
        """Return index of left child or None."""
        left = 2 * idx + 1
        return left if left < len(self._L) else None
    
    def idx_right(self, idx):
        """Return index of right child or None."""
        right = 2 * idx + 2
        return right if right < len(self._L) else None


    def idx_min_child(self, idx):
        """Return index of min child or None if no children."""
        left = self.idx_left(idx)
        right = self.idx_right(idx)
        if left is None:
            return None
        if right is None:
            return left
        return left if self._L[left] < self._L[right] else right     
        
    def insert(self, item, priority):
        """Add item with given priority to heap."""
        entry = Entry(item, priority)
        self._L.append(entry)
        idx = len(self._L) - 1
        self._idx[item] = idx
        self._upheap(idx)

    def remove_min(self):
        """Remove and return entry with smallest priority."""
        if not self._L:
            return None
        self._swap(0, len(self._L) - 1)
        min_entry = self._L.pop()
        del self._idx[min_entry.item]
        if self._L:
            self._downheap(0)
        return min_entry

    def change_priority(self, item, priority):
        """Change priority of given item and fix heap."""
        idx = self._idx.get(item)
        if idx is None:
            return None
        old_priority = self._L[idx].priority
        self._L[idx].priority = priority
        if priority < old_priority:
            self._upheap(idx)
        else:
            self._downheap(idx)
        return self._idx[item]

    def _swap(self, i, j):
        """Swap entries and update index mapping."""
        self._L[i], self._L[j] = self._L[j], self._L[i]
        self._idx[self._L[i].item] = i
        self._idx[self._L[j].item] = j

    def _upheap(self, idx):
        """Move item up until heap property is restored."""
        parent = self.idx_parent(idx)
        while parent is not None and self._L[idx] < self._L[parent]:
            self._swap(idx, parent)
            idx = parent
            parent = self.idx_parent(idx)

    def _downheap(self, idx):
        """Move item down until heap property is restored."""
        child = self.idx_min_child(idx)
        while child is not None and self._L[child] < self._L[idx]:
            self._swap(idx, child)
            idx = child
            child = self.idx_min_child(idx)

    @staticmethod
    def heapify(entries):
        """Build a heap from a list of Entry objects."""
        h = Heap()
        h._L = entries[:]
        h._idx = {entry.item: i for i, entry in enumerate(h._L)}
        for i in reversed(range(len(h._L) // 2)):
            h._downheap(i)
        return h