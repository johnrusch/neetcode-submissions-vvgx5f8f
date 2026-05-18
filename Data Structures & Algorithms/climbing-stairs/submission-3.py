class Solution:
    def climbStairs(self, n: int) -> int:
        # keep two vars to track amount of steps one and two steps away from current step
        # iterate through i -> n steps
        # 
        one, two = 1, 1
        for i in range(n):
            temp = one
            one += two
            two = temp

        return two