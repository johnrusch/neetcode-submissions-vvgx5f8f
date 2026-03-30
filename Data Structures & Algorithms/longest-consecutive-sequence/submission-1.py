class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        key = set(nums)
        max_seq = 0

        for num in nums:
            curr_seq = 0
            if num - 1 not in key:
                curr_seq = 1
                while num + 1 in key:
                    curr_seq += 1
                    num += 1

            max_seq = max(max_seq, curr_seq)

        return max_seq
