class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = nums[0]
        maxSum = nums[0]

        for n in nums[1:]:
            currSum = max(n, currSum + n)
            maxSum = max(currSum, maxSum)

        return maxSum