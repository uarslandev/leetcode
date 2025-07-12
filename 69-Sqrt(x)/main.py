class Solution:
    def mySqrt(self, x: int) -> int:
        sqr = 0
        for i in range (0,x):
            if i*i == x:
                sqr = i
                return sqr
            elif i*i > x:
                sqr = i - 1
                return sqr
