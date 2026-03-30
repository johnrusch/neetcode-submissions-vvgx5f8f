class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def helper(current, start_idx):
            if sum(current) == target:
                res.append(current.copy())
                return
            elif sum(current) > target:
                current = []
                return

            for i, num in enumerate(candidates[start_idx:]):
                if i > 0 and num == candidates[start_idx + (i - 1)]:
                    continue
                current.append(num)
                helper(current, start_idx + i + 1)
                current.pop()

        helper([], 0)
        return res
            