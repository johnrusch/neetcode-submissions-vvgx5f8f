class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = {}
        for num in nums:
            table[num] = 1 + table.get(num, 0)

        buckets = [[] for _ in range(len(nums) + 1)]

        for key, val in table.items():
            buckets[val].append(key)

        res = []
        for bucket in buckets[::-1]:
            for num in bucket:
                res.append(num)
                if len(res) == k:
                    return res
        
        return res