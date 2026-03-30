class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0

        l = 0
        r = len(height) - 1
        
        max_l = height[l]
        max_r = height[r]

        while l < r:
            if max_l <= max_r:
                trapped = min(max_l, max_r) - height[l]
                if trapped > 0:
                    res += trapped

                l += 1

                max_l = max(max_l, height[l])
            else:
                trapped = min(max_l, max_r) - height[r]
                if trapped > 0:
                    res += trapped

                r -= 1

                max_r = max(max_r, height[r])

        return res