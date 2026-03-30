class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(current, n_list):
            if len(current) == len(nums):
                res.append(current.copy())
                return

            for i, num in enumerate(n_list):
                current.append(num)
                helper(current, n_list[:i] + n_list[i + 1:])
                current.pop()

        helper([], nums)
        return res