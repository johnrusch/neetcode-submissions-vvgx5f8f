class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def helper(current, start_idx):
            res.append(current.copy())
            for i, num in enumerate(nums[start_idx:]):
                if i > 0 and num == nums[(start_idx + i) - 1]:
                    continue
                current.append(num)
                helper(current, start_idx + i + 1)
                current.pop()

        helper([], 0)
        return res
        