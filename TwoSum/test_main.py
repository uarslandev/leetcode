from main import Solution
from typing import List
import unittest

class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
        
    def test_case1(self):
        Input = [2,7,11,15]
        Target = 9
        Output = [0,1]

        self.assertEqual(self.sol.twoSum(Input, Target), Output)

    def test_case2(self):
        Input = [3,2,4]
        Target = 6
        Output = [1,2]

        self.assertEqual(self.sol.twoSum(Input, Target), Output)

    def test_case3(self):
        Input = [3,3]
        Target = 6
        Output = [0,1]

        self.assertEqual(self.sol.twoSum(Input, Target), Output)

if __name__ == '__main__':
    unittest.main()