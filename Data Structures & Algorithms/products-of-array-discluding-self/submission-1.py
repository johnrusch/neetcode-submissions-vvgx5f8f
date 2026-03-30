class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # set it up
        res = [1] * len(nums)
        prefix = 1

        # get prefix products
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]

        suffix = 1
        # get suffix products
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res
