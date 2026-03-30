class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        min_time = high
        while low <= high:
            mid = (low + high) // 2
            hours = 0
            for pile in piles:
                hours += int(pile / mid) + (pile % mid > 0)
            if hours <= h:
                min_time = mid
                high = mid - 1
            else:
                low = mid + 1

        return min_time
            