# what kind of things can you put the nums in?
#   a hash: dictionary that holds each num and the # of times seen
#   sorted: sort the list and iterate thru with two pointers
#   a list: list of buckets where index is frequency
#
# how can you use k while iterating? can you use k while iterating?
#   
# 
# make sure k is at least equal to len(nums), return nums if equal  
# iterate through list of nums
# put nums into hash
# iterate through hash items
# put each hash key into bucket with index being frequency of num
# go through buckets from the end, collecting k items to return in res
# [1, 2, 2, 3, 3, 3]
# {1: 1, 2: 2, 3: 3}

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k > len(nums):
            return [-1]
        elif k == nums:
            return nums

        hash_map = {}
        buckets = [[] for _ in range(len(nums) + 1)]
        res = []

        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        for num, freq in hash_map.items():
            buckets[freq].append(num)
        for bucket in buckets[::-1]:
            for num in bucket:
                res.append(num)
                if len(res) == k:
                    return res

        return res
