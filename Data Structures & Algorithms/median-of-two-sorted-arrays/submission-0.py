class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x, y = len(nums1), len(nums2)
        l, r = 0, x

        while l <= r:
            partX = (l + r) // 2
            partY = ((x + y + 1) // 2) - partX

            maxX = float('-inf') if partX == 0 else nums1[partX - 1]
            maxY = float('-inf') if partY == 0 else nums2[partY - 1]
            minX = float('inf') if partX == x else nums1[partX]
            minY = float('inf') if partY == y else nums2[partY]

            if maxX <= minY and maxY <= minX:
                if (x + y) % 2 == 0:
                    return (max(maxX, maxY) + min(minX, minY)) / 2
                else:
                    return max(maxX, maxY)
            elif maxX > minY:
                r = partX - 1
            else:
                l = partX + 1