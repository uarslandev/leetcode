import unittest
from main import lengthOfLongestSubstring

class LongestClassTest(unittest.TestCase):
    def test_3(self):
        self.assertEqual(lengthOfLongestSubstring("abcabcbb"), 3)

    def test_1(self):
        self.assertEqual(lengthOfLongestSubstring("bbbbb"), 1)

    def test_31(self):
        self.assertEqual(lengthOfLongestSubstring("pwwkew"), 3)

if __name__ == "__name__":
    unittest.mai()
