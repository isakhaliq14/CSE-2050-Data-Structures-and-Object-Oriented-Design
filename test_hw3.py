import unittest
from hw3 import generate_lists, find_common, find_common_efficient


class TestFunctions(unittest.TestCase):
    def test_generate_lists(self):
        size = 10
        list1, list2 = generate_lists(size)

        if len(list1) == size:
            print("List1 correct size")
        else:
            print("List1 incorrect size")

        if len(list2) == size:
            print("List2 correct size")
        else:
            print("List2 incorrect size")
        
        if len(list1) == len(set(list1)):
            print("List1 has unique elements")
        else:
            print("List1 doesn't have unique elements")

        if len(list2) == len(set(list2)):
            print("List2 has unique elements")
        else:
            print("List2 doesn't have unique elements")


    def test_find_common(self):
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
        common = find_common(list1, list2)
        if common == 9:
            print("find_common found common elements")
        else:
            print("find_common did not find common elements")


    def test_find_common_efficient(self):
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
        common = find_common_efficient(list1, list2)
        if common == 9:
            print("find_common_efficient found common elements")
        else:
            print("find_common_efficient did not find common elements")


if __name__ == '__main__':
    unittest.main()  