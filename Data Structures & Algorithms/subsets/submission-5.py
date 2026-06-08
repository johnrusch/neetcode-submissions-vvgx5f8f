class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(current, idx):
            if idx == len(nums):
                res.append(current.copy())
                return

            current.append(nums[idx])
            backtrack(current, idx + 1)
            current.pop()
            backtrack(current, idx + 1)

        backtrack([], 0)
        return res