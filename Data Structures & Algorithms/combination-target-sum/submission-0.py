class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def helper(current, start_idx):
            if sum(current) == target:
                res.append(current.copy())
                return

            if sum(current) > target:
                return

            for i, num in enumerate(nums[start_idx:]):
                current.append(num)
                helper(current, start_idx + i)
                current.pop()

        helper([], 0)
        return res