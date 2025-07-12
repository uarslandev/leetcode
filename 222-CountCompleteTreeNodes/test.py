import unittest
from main import Solution

class TestClass(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def tearDown(self):
        pass

    def test_feature1(self):
        self.assertEqual(self.s.countNodes([1,2,3,4,5,6]), 6)

    def test_feature2(self):
        self.assertEqual(self.s.countNodes([1]), 1)

    def test_feature3(self):
        self.assertEqual(self.s.countNodes([]), 0)

if __name__ == '__main__':
    unittest.main()
