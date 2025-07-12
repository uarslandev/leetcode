import unittest
from typing import List
from main import Solution

class TestClass(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def tearDown(self):
        pass

    def test_feature1(self):
        self.assertEqual(self.s.searchInsert([1,3,5,6], 5), 2)

    def test_feature2(self):
        self.assertEqual(self.s.searchInsert([1,3,5,6], 2), 1)

    def test_feature3(self):
        self.assertEqual(self.s.searchInsert([1,3,5,6], 7), 4)

if __name__ == '__main__':
    unittest.main()
