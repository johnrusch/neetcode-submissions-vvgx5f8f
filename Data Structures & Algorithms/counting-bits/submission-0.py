class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]

        for i in range(1, n + 1):
            num = i
            ones = 0
            while num:
                num &= (num - 1)
                ones += 1
            res.append(ones)

        return res