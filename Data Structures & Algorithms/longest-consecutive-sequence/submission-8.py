class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in nums:
            if (num - 1) not in num_set:
                cl = 1
                while (num + cl) in num_set:
                    cl += 1
            
                longest = max(longest, cl)

        return longest