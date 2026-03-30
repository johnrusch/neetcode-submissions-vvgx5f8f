class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupe_set = set()
        for num in nums:
            if num in dupe_set:
                return True
            else:
                dupe_set.add(num)
        return False