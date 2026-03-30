class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        floor = 0
        ceil = len(nums) - 1

        while floor <= ceil:
            mid = (floor + ceil) // 2
            if nums[mid] > target:
                ceil = mid - 1
            elif nums[mid] < target:
                floor = mid + 1
            else:
                return mid

        return -1