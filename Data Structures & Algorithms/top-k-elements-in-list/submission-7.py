class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        buckets = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for key, val in count.items():
            buckets[val].append(key)

        res = []
        for bucket in buckets[::-1]:
            for num in bucket:
                res.append(num)
                if len(res) == k:
                    return res

        return res