import unittest
from circularqueue import CircularQueue
from process import Process

class TestCircularQueue(unittest.TestCase):
    def assertNodeEqual(self, node, expected, expected_prev, expected_link):
        """Helper method to check node attributes."""
        self.assertEqual(node, expected)
        self.assertEqual(node.prev, expected_prev)
        self.assertEqual(node.link, expected_link)

    def test_init_empty(self):
        """Test initializing an empty circular queue."""
        cq = CircularQueue()
        self.assertEqual(len(cq), 0)
        self.assertIsNone(cq._head)

    def test_init_with_processes(self):
        """Test initializing a circular queue with processes."""
        p1 = Process('A', 100)
        p2 = Process('B', 200)
        cq = CircularQueue([p1, p2])
        self.assertEqual(len(cq), 2)
        self.assertEqual(cq._head, p1)
        self.assertNodeEqual(p1, p1, p2, p2)
        self.assertNodeEqual(p2, p2, p1, p1)

    def test_add_process_one(self):
        """Test adding one process to an empty circular queue."""
        cq = CircularQueue()
        p1 = Process('A', 100)
        cq.add_process(p1)
        self.assertEqual(len(cq), 1)
        self.assertNodeEqual(cq._head, p1, p1, p1)

    def test_add_process_two(self):
        """Test adding two processes to an empty circular queue."""
        cq = CircularQueue()
        p1 = Process('A', 100)
        p2 = Process('B', 200)
        cq.add_process(p1)
        cq.add_process(p2)
        self.assertEqual(len(cq), 2)
        self.assertNodeEqual(cq._head, p1, p2, p2)
        self.assertNodeEqual(p2, p2, p1, p1)

    def test_add_process_three(self):
        """Test adding three processes to an empty circular queue."""
        cq = CircularQueue()
        p1 = Process('A', 100)
        p2 = Process('B', 200)
        p3 = Process('C', 300)
        cq.add_process(p1)
        cq.add_process(p2)
        cq.add_process(p3)
        self.assertEqual(len(cq), 3)
        self.assertNodeEqual(cq._head, p1, p3, p2)
        self.assertNodeEqual(p2, p2, p1, p3)
        self.assertNodeEqual(p3, p3, p2, p1)

    def test_repr(self):
        """Test string representation of the circular queue."""
        p1 = Process('A', 100)
        p2 = Process('B', 200)
        cq = CircularQueue([p1, p2])
        self.assertEqual(repr(cq), "CircularQueue(Process(A, 100), Process(B, 200))")

    def test_remove_process_3_middle(self):
        """Test removing a process from the middle of a circular queue with 3 processes."""
        p1 = Process('A', 100)
        p2 = Process('B', 200)
        p3 = Process('C', 300)
        cq = CircularQueue([p1, p2, p3])
        removed = cq.remove_process(p2)
        self.assertEqual(removed, p2)
        self.assertEqual(len(cq), 2)
        self.assertNodeEqual(cq._head, p1, p3, p3)
        self.assertNodeEqual(p3, p3, p1, p1)

    def test_remove_process_3_head(self):
        """Test removing the head process from a circular queue with 3 processes."""
        p1 = Process('A', 100)
        p2 = Process('B', 200)
        p3 = Process('C', 300)
        cq = CircularQueue([p1, p2, p3])
        removed = cq.remove_process(p1)
        self.assertEqual(removed, p1)
        self.assertEqual(len(cq), 2)
        self.assertNodeEqual(cq._head, p2, p3, p3)
        self.assertNodeEqual(p3, p3, p2, p2)

    def test_remove_process_3_final(self):
        """Test removing the final process from a circular queue with 3 processes."""
        p1 = Process('A', 100)
        p2 = Process('B', 200)
        p3 = Process('C', 300)
        cq = CircularQueue([p1, p2, p3])
        removed = cq.remove_process(p3)
        self.assertEqual(removed, p3)
        self.assertEqual(len(cq), 2)
        self.assertNodeEqual(cq._head, p1, p2, p2)
        self.assertNodeEqual(p2, p2, p1, p1)

    def test_remove_process_1(self):
        """Test removing the only process from a circular queue."""
        p1 = Process('A', 100)
        cq = CircularQueue([p1])
        removed = cq.remove_process(p1)
        self.assertEqual(removed, p1)
        self.assertEqual(len(cq), 0)
        self.assertIsNone(cq._head)

    def test_kill_3_middle(self):
        """Test killing a process in the middle of a circular queue with 3 processes."""
        p1 = Process('A', 100)
        p2 = Process('B', 200)
        p3 = Process('C', 300)
        cq = CircularQueue([p1, p2, p3])
        killed = cq.kill('B')
        self.assertEqual(killed, p2)
        self.assertEqual(len(cq), 2)
        self.assertNodeEqual(cq._head, p1, p3, p3)
        self.assertNodeEqual(p3, p3, p1, p1)

unittest.main()