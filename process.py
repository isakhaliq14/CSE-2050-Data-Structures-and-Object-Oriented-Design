class Process:
    def __init__(self, pid, cycles = 100):
        """Initialize process with pid and optional cycles."""
        self.pid = pid
        self.cycles = cycles
        self.link = None
        self.prev = None

    def __eq__(self, other):
        """Two processes are equal if they have the same pid."""
        return self.pid == other.pid

    def __repr__(self):
        """Returns a string representation of the Process object."""
        return f"Process({self.pid}, {self.cycles})"
    
if __name__ == '__main__':
    p1 = Process('send_email') 
    p2 = Process('A', 400) 
    print(p1.pid, p1.cycles, p1.link, p1.prev)
    print(p2.pid, p2.cycles, p2.link, p2.prev)
    print(p1)


    