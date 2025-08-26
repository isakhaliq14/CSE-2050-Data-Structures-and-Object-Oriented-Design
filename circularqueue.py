from process import Process

class CircularQueue:
    """A circular queue to allow us to run processes turn-by-turn"""
    
    def __init__(self, processes = None):
        """Initialize the circular queue."""
        self._head = None
        self._len = 0
        self._d_processes = {}
        if processes:
            for process in processes:
                self.add_process(process)

    def __len__(self):
        """Return the number of processes in the queue."""
        return self._len

    def __repr__(self):
        """String representation of the circular queue."""
        if self._head is None:
            return "CircularQueue()"
        processes = []
        current = self._head
        for _ in range(self._len):
            processes.append(repr(current))
            current = current.link
        return f"CircularQueue({', '.join(processes)})"

    def add_process(self, process):
        """Add a process to the end of the queue."""
        if self._head is None:
            self._head = process
            process.link = process
            process.prev = process
        else:
            last = self._head.prev
            last.link = process
            process.prev = last
            process.link = self._head
            self._head.prev = process
        self._d_processes[process.pid] = process
        self._len += 1

    def remove_process(self, process):
        """Remove a process from the queue."""
        if self._len == 1:
            self._head = None
        else:
            process.prev.link = process.link
            process.link.prev = process.prev
            if process == self._head:
                self._head = process.link
        self._d_processes.pop(process.pid)
        self._len -= 1
        return process

    def kill(self, pid):
        """Remove and return a process with the given pid."""
        if pid in self._d_processes:
            process = self._d_processes[pid]
            return self.remove_process(process)
        return None

    def run(self, n_cycles):
        """Runs circular queue for n_cycles, giving each process 1 cycle at a time"""
        n_remaining = n_cycles
        return_strings = []   # Using an intermediate list since appending to a string is O(n)

        while n_remaining:
            self._head.cycles -= 1

            if self._head.cycles == 0:
                return_strings.append(f"{self._head.pid} finished after {n_cycles-n_remaining+1} computational cycles.")
                self.remove_process(self._head)

            else:
                self._head = self._head.link
            
            n_remaining -= 1

        return '\n'.join(return_strings)
    

if __name__ == '__main__':
    p1 = Process('send_email', 250)
    p2 = Process('open_word', 100)
    p3 = Process('run_simulation', 1000)
    cq = CircularQueue([p1, p2, p3])

    print(repr(cq))

    c1 = CircularQueue()
    c1.add_process(Process("send_email"))
    c1.add_process(Process("open_word"))
    c1.add_process(Process("simulate_transistor_fabrication"))

    print(len(c1))
    print(c1._d_processes["open_word"])
    c1.kill("open_word")
    print(len(c1))