class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False

        num_map = set()

        for num in nums:
            if num in num_map:
                return True

            num_map.add(num)

        return False