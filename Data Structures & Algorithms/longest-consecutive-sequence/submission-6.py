class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_map = set(nums)
        longest = 0

        for num in nums:
            if (num - 1) not in num_map:
                curr_len = 1
                while (num + curr_len) in num_map:
                    curr_len += 1
                longest = max(longest, curr_len)

        return longest