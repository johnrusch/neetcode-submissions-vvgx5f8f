class Solution:
    def hammingWeight(self, n: int) -> int:
        # logic and-ing with n - 1
        res = 0
        while n:
            n &= (n - 1)
            res += 1
        return res
