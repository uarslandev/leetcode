import unittest

from typing import List
from main import Solution

class TestClass(unittest.TestCase):
    def setUp(self):
        S = Solution()

    def tearDown(self):
        pass

    def test_feature1(self):
        self.assertEqual(S.searchInsert([1,3,5,6], 5), 2)

if __name__ == '__main__':
    unittest.main()

