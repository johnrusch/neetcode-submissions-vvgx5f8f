class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(idx, current, currSum):
            if currSum == target:
                res.append(current.copy())
                return
            elif idx >= len(candidates) or currSum > target:
                return

            for j in range(idx, len(candidates)):
                if j > idx and candidates[j] == candidates[j - 1]:
                    continue
                if currSum + candidates[j] > target:
                    break

                current.append(candidates[j])
                backtrack(j + 1, current, currSum + candidates[j])
                current.pop()

            
        backtrack(0, [], 0)
        return res

            
            