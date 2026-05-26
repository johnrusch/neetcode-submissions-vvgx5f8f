class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
    
        for key, val in count.items():
            buckets[val].append(key)

        res = []

        for bucket in buckets[::-1]:
            for num in bucket:
                if len(res) < k:
                    res.append(num)
                else:
                    return res

        return res