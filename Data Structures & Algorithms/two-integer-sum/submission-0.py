# Create dictionary to keep track of nums seen and their indexes
# Go through list of nums
# Calculate the num needed in the list to reach target
# Look for complement in dictionary
# Add num with its index to dictionary

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            num = nums[i]
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i

        return [-1, -1]