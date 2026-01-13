from typing import List
# a + b = target -> b = target - a
class Solution:
    def romanToInt(self, s: str) -> int:
        dictionary = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sum = 0
        i = 0
        while i < len(s):
            val = dictionary[s[i]]
            if i+1 < len(s):
                nextVal = dictionary[s[i+1]]
                if val < nextVal:
                    sum += nextVal - val
                    i+=2
                    continue
            sum += val
            i+=1
        return sum