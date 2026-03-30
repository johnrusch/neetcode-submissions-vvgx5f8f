class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        key = set(nums)
        max_seq = 0

        for num in nums:
            if num - 1 not in key:
                length = 1
                while num + length in key:
                    length += 1

                max_seq = max(max_seq, length)

        return max_seq
