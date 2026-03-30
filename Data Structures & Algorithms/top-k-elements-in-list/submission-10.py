class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        num_map = {}

        for num in nums:
            num_map[num] = num_map.get(num, 0) + 1

        for num, val in num_map.items():
            buckets[val].append(num)

        res = []

        for bucket in buckets[::-1]:
            for n in bucket:
                if len(res) < k:
                    res.append(n)
                else:
                    return res

        return res