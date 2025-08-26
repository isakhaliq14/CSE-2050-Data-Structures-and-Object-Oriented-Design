class Entry:
    def __init__(self, item, priority):
        """Create an entry with item and priority."""
        self.item = item
        self.priority = priority

    def __eq__(self, other):
        """Check if priorities are equal."""
        return self.priority == other.priority

    def __lt__(self, other):
        """Check if this priority is less than the other."""
        return self.priority < other.priority

    def __le__(self, other):
        """Check if this priority is less than or equal to the other."""
        return self.priority <= other.priority

    def __repr__(self):
        """Return Entry(item, priority) as a string."""
        return f"Entry(item={self.item}, priority={self.priority})"