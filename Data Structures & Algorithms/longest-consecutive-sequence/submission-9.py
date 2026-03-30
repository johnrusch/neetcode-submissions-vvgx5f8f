class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0

        for num in seen:
            curr_len = 1
            while num - 1 in seen:
                curr_len += 1
                num -= 1

            longest = max(longest, curr_len)

        return longest