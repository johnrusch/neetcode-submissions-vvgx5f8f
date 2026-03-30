class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_key = set()

        for num in nums:
            if num in num_key:
                return True
            else:
                num_key.add(num)

        return False
