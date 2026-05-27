class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in seen:
                current = 1
                while num + 1 in seen:
                    current += 1
                    num += 1
            
                longest = max(longest, current)

        return longest