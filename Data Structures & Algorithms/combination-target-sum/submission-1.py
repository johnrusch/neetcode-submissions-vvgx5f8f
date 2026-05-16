class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        seen = set()

        def backtrack(i, current):
            if sum(current) > target:
                return
            if sum(current) == target:
                if tuple(current) not in seen:
                    res.append(current.copy())
                    seen.add(tuple(current))
            if i >= len(nums):
                return

            current.append(nums[i])
            backtrack(i, current)
            current.pop()
            backtrack(i + 1, current)
        
        backtrack(0, [])

        return res