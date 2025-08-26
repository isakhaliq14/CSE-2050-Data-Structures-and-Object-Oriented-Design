# See assignment for class attributes.
# Remember to include docstrings.
# Start with unittests

class LocalRecord:
    def __init__(self, pos, max=None, min=None, precision = 0):
        lat, lon = pos
        self.pos = (round(lat, precision), round(lon, precision))
        self.max = max
        self.min = min

    def add_report(self, temp):
        """Update min/max temperatures based on new report."""
        if self.max is None or temp > self.max:
            self.max = temp
        if self.min is None or temp < self.min:
            self.min = temp

    def __eq__(self, other):
        """Equality based on rounded position."""
        return isinstance(other, LocalRecord) and self.pos == other.pos

    def __hash__(self):
        """Hash based on rounded position tuple."""
        return hash(self.pos)

    def __repr__(self):
        return f"Record(pos={self.pos}, max={self.max}, min={self.min})"

class RecordsMap:
    def __init__(self):
        self._size = 0
        self._capacity = 8
        self._table = [None] * self._capacity

    def __len__(self):
        return self._size
    
    def _index(self, key):
        """Compute index in the table using hash."""
        return hash(key) % self._capacity

    def add_report(self, pos, temp):
        """Add a temperature report to the appropriate LocalRecord."""
        record = LocalRecord(pos)
        index = self._index(record)

        while self._table[index] is not None:
            if self._table[index] == record:
                self._table[index].add_report(temp)
                return
            index = (index + 1) % self._capacity

        record.add_report(temp)
        self._table[index] = record
        self._size += 1

        if self._size / self._capacity > 0.7:
            self._rehash(self._capacity * 2)

    def __getitem__(self, pos):
        """Return (min, max) for the position, or raise KeyError."""
        record = LocalRecord(pos)
        index = self._index(record)

        probes = 0
        while self._table[index] is not None:
            if self._table[index] == record:
                return (self._table[index].min, self._table[index].max)
            index = (index + 1) % self._capacity
            probes += 1
            if probes > self._capacity:
                break

        raise KeyError(f"No records for pos {record.pos}.")
  
    def __contains__(self, pos):
        """Return True if position is in the map, False otherwise."""
        record = LocalRecord(pos)
        index = self._index(record)

        probes = 0
        while self._table[index] is not None:
            if self._table[index] == record:
                return True
            index = (index + 1) % self._capacity
            probes += 1
            if probes > self._capacity:
                break

        return False

    def _rehash(self, m_new):
        """Resize the internal table and reinsert all records."""
        old_table = self._table
        self._capacity = m_new if m_new else 2 * self._capacity
        self._table = [None] * self._capacity
        self._size = 0

        for entry in old_table:
            if entry:
                self.add_report(entry.pos, entry.min)
                if entry.max != entry.min:
                    self.add_report(entry.pos, entry.max)