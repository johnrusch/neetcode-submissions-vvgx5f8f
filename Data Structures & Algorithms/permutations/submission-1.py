class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # if len(curr) == len(nums) add copy of curr to res
        # 
        res = []

        def backtrack(n_list, curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for i, num in enumerate(n_list):
                curr.append(num)
                backtrack(n_list[:i] + n_list[i + 1:], curr)
                curr.pop()

        backtrack(nums, [])

        return res