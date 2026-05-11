class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        int_map = {}

        for i, num in enumerate(nums):
            comp = target - num
            if comp in int_map:
                return [int_map[comp], i]

            int_map[num] = i

        return [-1]