from main import Solution
from typing import List
import unittest

class TestMajorityElement(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
        
    def test_case1(self):
        input = [3,2,3]
        output = 3

        self.assertEqual(self.sol.majorityElement(input), output)

    def test_case2(self):
        input = [2,2,1,1,1,2,2]
        output = 2

        self.assertEqual(self.sol.majorityElement(input), output)

    def test_case3(self):
        input = [3,3,4]
        output = 3

        self.assertEqual(self.sol.majorityElement(input), output)

if __name__ == '__main__':
    unittest.main()