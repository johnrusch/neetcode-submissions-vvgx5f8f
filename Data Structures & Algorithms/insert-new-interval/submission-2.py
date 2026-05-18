class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # iterate through intervals
        # all about edge cases here
        # 1. end of newinterval comes before start of current,
        # add newinterval to res and immediately return res + the rest of intervals
        # 2. start of newinterval comes after end of current,
        # add current interval to res
        # 3. current interval overlaps,
        # overwrite newinterval with min of starts and max of ends
        # after iteration, append newinterval in case we didn't hit first case

        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        res.append(newInterval)

        return res