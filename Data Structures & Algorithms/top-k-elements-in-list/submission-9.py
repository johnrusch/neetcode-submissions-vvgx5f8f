class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_map = {}
        buckets = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            num_map[num] = 1 + num_map.get(num, 0)

        for key, val in num_map.items():
            buckets[val].append(key)

        res = []
        for bucket in buckets[::-1]:
            for num in bucket:
                res.append(num)
                if len(res) == k:
                    return res


        return res