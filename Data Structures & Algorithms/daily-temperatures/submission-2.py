class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return [-1]

        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                last_i, last_t = stack.pop()
                res[last_i] = i - last_i

            stack.append([i, t])


        return res