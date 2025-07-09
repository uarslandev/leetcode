import unittest
from typing  import List
from main import Solution

class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.S = Solution()

    def tearDown(self):
        pass

    def test_feature(self):
        self.assertEqual(self.S.search([-1, 0, 3, 5, 9, 12], 9), 4)

    def test_feature2(self):
        self.assertEqual(self.S.search([-1,0,3,5,9,12], 2), -1)

    def test_feature3(self):
        self.assertEqual(self.S.search([5], 5), 0)
