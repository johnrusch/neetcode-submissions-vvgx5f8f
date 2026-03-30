class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return [-1]

        res, stack = [0] * len(temperatures), []

        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                last_i = stack.pop()
                res[last_i] = i - last_i

            stack.append(i)

        return res