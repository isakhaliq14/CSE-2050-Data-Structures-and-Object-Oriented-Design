import unittest
from dictionary_bst import DictionaryBST

class TestDictionaryBST(unittest.TestCase):
    def setUp(self):
        self.dictionary = DictionaryBST()
        self.dictionary.insert("banana", "A yellow tropical fruit.")
        self.dictionary.insert("apple", "A fruit that grows on trees.")
        self.dictionary.insert("cherry", "A small, round, red fruit.")

    def test_insert_and_search(self):
        self.assertEqual(self.dictionary.search("banana"), "A yellow tropical fruit.")
        self.assertEqual(self.dictionary.search("apple"), "A fruit that grows on trees.")
        self.assertEqual(self.dictionary.search("cherry"), "A small, round, red fruit.")
        self.assertIsNone(self.dictionary.search("orange"))

    def test_update_meaning(self):
        self.dictionary.insert("apple", "Updated meaning.")
        self.assertEqual(self.dictionary.search("apple"), "Updated meaning.")

    def test_print_alphabetical(self):
        expected = [
            ("apple", "A fruit that grows on trees."),
            ("banana", "A yellow tropical fruit."),
            ("cherry", "A small, round, red fruit.")
        ]
        self.assertEqual(self.dictionary.print_alphabetical(), expected)

if __name__ == '__main__':
    unittest.main()