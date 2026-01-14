from main import Solution, ListNode
from typing import List
import unittest

class TestHasCycle(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
        
    def test_case1(self):
        a = ListNode(3)
        b = ListNode(2)
        c = ListNode(0)
        d = ListNode(-4)

        a.next = b
        b.next = c
        c.next = d
        d.next = b

        self.assertTrue(self.sol.hasCycle(a))

    def test_case2(self):
        a = ListNode(1)

        self.assertFalse(self.sol.hasCycle(a))
if __name__ == '__main__':
    unittest.main()