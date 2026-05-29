class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        i = 0
        current_end = 0
        farthest = 0

        while i < len(nums) - 1:
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest

            i += 1

        return jumps