from main import Solution
from typing import List
import unittest
class TestRomanToInteger(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
        
    def test_case1(self):
        Input = "III"
        Output = 3

        self.assertEqual(self.sol.romanToInt(Input), Output)

    def test_case2(self):
        Input = "LVIII"
        Output = 58

        self.assertEqual(self.sol.romanToInt(Input), Output)

    def test_case3(self):
        Input = "MCMXCIV"
        Output = 1994

        self.assertEqual(self.sol.romanToInt(Input), Output)

if __name__ == '__main__':
    unittest.main()