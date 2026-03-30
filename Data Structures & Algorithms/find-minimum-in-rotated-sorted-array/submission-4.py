class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_seen = float("inf")

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                min_seen = min(min_seen, nums[mid])
                r = mid - 1

        return min_seen