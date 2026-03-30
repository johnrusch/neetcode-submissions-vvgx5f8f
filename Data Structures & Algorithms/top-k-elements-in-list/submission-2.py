class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        buckets = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        for n, c in counts.items():
            buckets[c].append(n)

        res = []
        for i in range(len(buckets) - 1, -1, -1):
            for j in buckets[i]:
                res.append(j)
                if len(res) == k:
                    return res

        return [-1]
        