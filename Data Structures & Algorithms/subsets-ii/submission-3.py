class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(idx, current):
            res.append(current.copy())
            for i, num in enumerate(nums[idx:]):
                if i > 0 and num == nums[(idx + i) - 1]:
                    continue
                current.append(num)
                backtrack(idx + i + 1, current)
                current.pop()

        backtrack(0, [])
        return res