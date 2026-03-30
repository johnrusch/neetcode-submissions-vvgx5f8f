class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        combos = set()

        def helper(current, start_idx):
            if start_idx == len(nums):
                if tuple(current) not in combos:
                    combos.add(tuple(current))

            for i, num in enumerate(nums[start_idx:]):
                current.append(num)
                if tuple(current) not in combos:
                    combos.add(tuple(current))
                helper(current, start_idx + i + 1)
                current.pop()

        helper([], 0)
        res = [list(t) for t in combos]
        res.append([])
        return res
        