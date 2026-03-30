# create a dictionary
# iterate through list
#   look for the complement to current num in dictionary
#   add num to dictionary

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp_map = {}

        for i in range(len(nums)):
            num = nums[i]
            comp = target - num
            if comp in comp_map:
                return [comp_map[comp], i]

            comp_map[num] = i

        return [-1]