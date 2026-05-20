class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []

        def backtrack(i, current, currSum):
            if currSum == target:
                res.append(current.copy())
                return
            elif i >= len(candidates) or sum(current) > target:
                current = []
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if currSum + candidates[j] > target:
                    break
                current.append(candidates[j])
                backtrack(j + 1, current, currSum + candidates[j])
                current.pop()


        backtrack(0, [], 0)
        return res