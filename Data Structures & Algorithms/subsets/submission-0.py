class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for i, num in enumerate(nums):
            for s in res[:]:
                new_subset = s + [num]
                res.append(new_subset)
            
        return res
