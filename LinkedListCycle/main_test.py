from main import Solution, ListNode
from typing import List
import unittest

class TestHasCycle(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
        
    def test_case1(self):
        head = [3,2,0,-4]
        pos = 1
        Output = True

        self.listNode = ListNode(head)

        self.assertEqual(self.sol.hasCycle(self.listNode)), Output)

if __name__ == '__main__':
    unittest.main()