class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # [1, 2, 0, 1, 0]
        lastIdx = len(nums) - 1
        currIdx = lastIdx - 1

        while currIdx >= 0:
            gap = lastIdx - currIdx
            if nums[currIdx] >= gap:
                lastIdx = currIdx
            currIdx -= 1

        return lastIdx == 0