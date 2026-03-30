class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        combos = set()

        def helper(current, start_idx):
            if sum(current) == target and tuple(current) not in combos:
                combos.add(tuple(current))
                return
            elif sum(current) > target:
                current = []
                return

            for i, num in enumerate(candidates[start_idx:]):
                current.append(num)
                helper(current, start_idx + i + 1)
                current.pop()

        helper([], 0)
        return [list(t) for t in combos]
            