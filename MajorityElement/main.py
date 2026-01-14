from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        maj = 0
        for i, val in enumerate(nums):
            if val in hashmap:
                hashmap[val] += 1
                continue
            hashmap[val] = 1
        maj = max(hashmap, key=hashmap.get)
        return maj