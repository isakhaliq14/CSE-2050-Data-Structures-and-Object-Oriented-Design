# Import what you need
# Include unittests here. Focus on readability, including comments and docstrings.
import unittest
from RecordsMap import LocalRecord, RecordsMap

class TestLocalRecord(unittest.TestCase):
    def test_init(self):
        """Test initialization of LocalRecord with correct rounding and initial min/max values."""
        record = LocalRecord((41.8067, -72.2522))
        self.assertEqual(record.pos, (42.0, -72.0))
        self.assertIsNone(record.min)
        self.assertIsNone(record.max)

    def test_hash(self):
        """Test that two LocalRecords with the same rounded coordinates produce the same hash."""
        r1 = LocalRecord((41.81, -72.25))
        r2 = LocalRecord((41.89, -72.22))
        self.assertEqual(hash(r1), hash(r2))

    def test_eq(self):
        """Test that two LocalRecords with the same rounded coordinates are considered equal."""
        r1 = LocalRecord((41.8067, -72.2522))
        r2 = LocalRecord((41.8097, -72.1473))
        r3 = LocalRecord((41.3, -72.4))  
        self.assertEqual(r1, r2)
        self.assertNotEqual(r1, r3)

    def test_add_report(self):
        """Test that add_report correctly updates the min and max temperatures."""
        r = LocalRecord((41.8, -72.2))
        r.add_report(30)
        self.assertEqual(r.min, 30)
        self.assertEqual(r.max, 30)

        r.add_report(25)
        self.assertEqual(r.min, 25)
        self.assertEqual(r.max, 30)

        r.add_report(35)
        self.assertEqual(r.min, 25)
        self.assertEqual(r.max, 35)


class TestRecordsMap(unittest.TestCase):
    def test_add_one_report(self):
        """Test adding a single report and accessing via get, contains, and len."""
        rm = RecordsMap()
        p = (41.8067, -72.2522)

        self.assertEqual(len(rm), 0)
        self.assertFalse(p in rm)

        rm.add_report(p, 20)
        self.assertEqual(len(rm), 1)
        self.assertTrue(p in rm)
        self.assertEqual(rm[p], (20, 20))

    def test_add_many_reports(self):
        """Test adding many reports and verify correctness of length, values, and access methods."""
        rm = RecordsMap()
        base_lat = 41.0
        base_long = -72.0

        for i in range(100):
            lat = base_lat + (i % 5) * 0.1
            long = base_long + (i % 5) * 0.1
            pos = (lat, long)
            temp = 20 + i
            rm.add_report(pos, temp)

        self.assertLessEqual(len(rm), 25)

        sample_pos = (41.3, -71.8)
        self.assertTrue(sample_pos in rm or round(sample_pos[0]) == 41 and round(sample_pos[1]) == -72)

        for rec in rm._table:
            if rec is not None:
                self.assertLessEqual(rec.min, rec.max)

# You need to add a line here to run the unittests
if __name__ == "__main__":
    unittest.main()