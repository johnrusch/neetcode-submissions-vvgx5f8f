# return false if list is smaller than 2
# create set as a hash map
# iterate through list, adding to set and checking if num exists

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False

        hash_map = set()

        for num in nums:
            if num in hash_map:
                return True

            hash_map.add(num)

        return False