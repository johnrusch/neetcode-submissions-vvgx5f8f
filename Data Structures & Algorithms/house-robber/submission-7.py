class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1, prev2 = 0, 0

        for i, num in enumerate(nums):
            temp = prev1
            prev1 = max(prev1, num + prev2)
            prev2 = temp

        return max(prev1, prev2)