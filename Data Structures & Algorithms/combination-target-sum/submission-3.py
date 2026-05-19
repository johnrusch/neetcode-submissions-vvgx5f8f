class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, current):
            if sum(current) == target:
                res.append(current.copy())
                return
            if sum(current) > target or i >= len(nums):
                return

            current.append(nums[i])
            backtrack(i, current)
            current.pop()
            backtrack(i + 1, current)

        backtrack(0, [])
        return res