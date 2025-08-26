import unittest
from trib import trib

class TestTrib(unittest.TestCase):
    def test_first_ten(self):
        """Tests the first 10 numbers in the tribonacci series"""
        solutions = {0: 0, 1: 1, 2: 1, 3: 2, 4: 4, 5: 7, 6: 13, 7: 24, 8: 44, 9: 81}
        for k in solutions:
            self.assertEqual(trib(k), solutions[k])
    
    def test_trib_100(self):
        """Tests that trib(100) returns the correct value"""
        self.assertEqual(trib(100), 28992087708416717612934417)

if __name__ == "__main__":
    unittest.main()

