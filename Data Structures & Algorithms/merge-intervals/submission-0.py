class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the input array by start_i
        # iterate through the array from 0 -> n - 1
        # for each, check to see if end_i overlaps with next interval
        # 
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        
        for start, end in intervals[1:]:
            lastEnd = res[-1][1]

            if start <= lastEnd:
                res[-1][1] = max(lastEnd, end)
            else:
                res.append([start, end])

        return res