###############################################################################
# init, and repr  are implemented for you. You should implement the other     #
# methods recursively.                                                        #
###############################################################################
class Node:
    """Recursively implements Linked List functionality."""
    def __init__(self, data, link=None):
        """Instantiates a new Node with given data."""
        self.data = data
        self.link = link

    def __repr__(self):
        """Returns string representation of node."""
        return f"Node({self.data})"
    
    def __len__(self):
        """Recursively calculates length of sublist starting at this node."""
        return 1 if self.link is None else 1 + len(self.link)

    def get_tail(self):
        """Recursively finds the data stored in the tail of this sublist."""
        return self.data if self.link is None else self.link.get_tail()
    
    def add_last(self, data):
        """Recursively adds to end of this sublist."""
        if self.link is None:
            self.link = Node(data)
        else:
            self.link.add_last(data)
    
    def total(self):
        """Recursively adds all items."""
        return self.data if self.link is None else self.data + self.link.total()
    
    def remove_last(self):
        """Recursively removes last item in sublist.
            Returns a tuple of (new_head, data)."""
        if self.link is None:
            return None, self.data
        self.link, tail_data = self.link.remove_last()
        return self, tail_data
    
    def reverse(self, prev=None):
        """Recursively reverses the list."""
        if self.link is None:
            self.link = prev
            return self
        new_head = self.link.reverse(self)
        self.link = prev
        return new_head