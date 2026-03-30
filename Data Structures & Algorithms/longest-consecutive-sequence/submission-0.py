# make set of nums list
# create max sequence variable
# go through nums list finding sequences and keeping track of the biggest
# return max sequence

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2: 
            return len(nums)

        nums_set = set(nums)

        max_seq = 0

        for num in nums:
            if num - 1 not in nums_set:
                curr_seq = 1
                n = num
                while n + 1 in nums_set:
                    curr_seq += 1
                    n = n + 1

                max_seq = max(max_seq, curr_seq)

        return max_seq