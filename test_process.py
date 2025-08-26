import unittest
from process import Process

class TestProcess(unittest.TestCase):
    def test_init_name(self):
        """Test creating a process with just a name."""
        p = Process('send_email')
        self.assertEqual(p.pid, 'send_email')
        self.assertEqual(p.cycles, 100)
        self.assertIsNone(p.link)
        self.assertIsNone(p.prev)

    def test_init_name_and_cycles(self):
        """Test creating a process with a name and cycles."""
        p = Process('A', 400)
        self.assertEqual(p.pid, 'A')
        self.assertEqual(p.cycles, 400)
        self.assertIsNone(p.link)
        self.assertIsNone(p.prev)

    def test_eq(self):
        """Test eq method"""
        p1 = Process('A')
        p2 = Process('A')
        p3 = Process('B')
        self.assertEqual(p1, p2)
        self.assertNotEqual(p1, p3)

    def test_repr(self):
        """Test repr method"""
        p = Process('send_email', 250)
        self.assertEqual(repr(p), "Process(send_email, 250)")

unittest.main()