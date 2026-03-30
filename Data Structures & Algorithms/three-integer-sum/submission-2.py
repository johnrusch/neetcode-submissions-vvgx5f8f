class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[-1]]

        nums.sort()
        res = []
        i = 0

        while i < len(nums) - 2:
            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
            
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        
        return res
