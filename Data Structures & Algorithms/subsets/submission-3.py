class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # backtrack fn takes in i and current subset
        # if i == len(nums), add copy of current subset
        res = []

        def backtrack(i, curr):
            if i == len(nums):
                res.append(curr.copy())
                return
            
            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()
            backtrack(i + 1, curr)

        backtrack(0, [])

        return res
