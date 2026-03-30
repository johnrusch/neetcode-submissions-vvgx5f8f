class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_key = {}
        res = []

        for num in nums:
            hash_key[num] = hash_key.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for key in hash_key:
            buckets[hash_key[key]].append(key)
        for bucket in buckets[::-1]:
            for num in bucket:
                if len(res) < k:
                    res.append(num)
                else:
                    return res

        return res

        