class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        sorted_queries = sorted(enumerate(queries), key=lambda q: q[1])
        res = [-1] * len(queries)
        heap = []
        i = 0
        for orig_idx, q in sorted_queries:
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(heap, ((r - l) + 1, r))
                i += 1

            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            if heap:
                res[orig_idx] = heap[0][0]

        return res

