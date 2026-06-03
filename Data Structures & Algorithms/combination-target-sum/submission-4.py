class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(current, currSum, idx):
            if currSum == target:
                res.append(current.copy())
                return
            elif currSum > target or idx >= len(nums):
                return

            current.append(nums[idx])
            backtrack(current, currSum + nums[idx], idx)
            current.pop()
            backtrack(current, currSum, idx + 1)

        backtrack([], 0, 0)
        return res