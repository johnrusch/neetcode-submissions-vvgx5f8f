class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: i[0])

        res = 0
        prevEnd = intervals[0][1]
        for interval in intervals[1:]:
            print(interval, prevEnd)
            if interval[0] < prevEnd:
                res += 1
                prevEnd = min(prevEnd, interval[1])
            else:
                prevEnd = interval[1]

        return res