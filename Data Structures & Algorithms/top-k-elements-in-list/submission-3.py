class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        key = {}
        buckets = [[] for _ in range(len(nums) + 1)]
        res = []

        for num in nums:
            key[num] = key.get(num, 0) + 1

        print(key)
        for j, v in key.items():
            print(buckets)
            buckets[v].append(j)

        for bucket in range(len(buckets) - 1, -1, -1):
            for n in buckets[bucket]:
                res.append(n)
                if len(res) == k:
                    return res

        return res