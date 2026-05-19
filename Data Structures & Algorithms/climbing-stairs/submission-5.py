class Solution:
    def climbStairs(self, n: int) -> int:
        # memory: since this is fibonacci, adding two steps together
        prev1, prev2 = 1, 1
        for i in range(n):
            temp = prev1
            prev1 += prev2
            prev2 = temp
            print(prev2)

        return prev2