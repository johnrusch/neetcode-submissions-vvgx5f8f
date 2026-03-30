class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]

        heapq.heapify(max_heap)

        while len(max_heap) > 1: 
            a, b = heapq.heappop(max_heap), heapq.heappop(max_heap)
            if a < b:
                heapq.heappush(max_heap, a - b)
            
        max_heap.append(0)
        return abs(max_heap[0])