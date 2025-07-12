import unittest
from main import Solution

class TestClass(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        self.assertEqual(self.s.mySqrt(4), 2)

    def test_2(self):
        self.assertEqual(self.s.mySqrt(8), 2)

    def test_3(self):
        self.assertEqual(self.s.mySqrt(0), 0)

    def test_4(self):
        self.assertEqual(self.s.mySqrt(1), 1)

if __name__ == '__main__':
    unittest.main()

