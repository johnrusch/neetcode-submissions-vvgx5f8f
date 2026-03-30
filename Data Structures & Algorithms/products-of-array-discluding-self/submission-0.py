
# initialize result array
# set a prefix amount of 1
# iterate through the list of nums from left to right
#   generating the prefix value in the result array as we go
# iterate through the list from right to left
#   generating the suffix value in the result array as we go
# return result array

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for _ in range(len(nums))]
        prefix = 1
        for i in range(len(nums)):
            res[i] = res[i] * prefix
            prefix = prefix * nums[i]

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = res[i] * suffix
            suffix = suffix * nums[i]

        return res