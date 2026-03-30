class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        key = set()
        for num in nums:
            if num in key:
                return True
            else:
                key.add(num)

        return False