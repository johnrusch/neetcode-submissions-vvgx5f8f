class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return -1

        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                last_i, last_h = stack.pop()
                area = (i - last_i) * last_h
                max_area = max(max_area, area)
                start = last_i
            stack.append([start, h])

        while stack:
            last_i, last_h = stack.pop()
            area = (len(heights) - last_i) * last_h
            max_area = max(max_area, area)

        return max_area