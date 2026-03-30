class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_b, max_b = 1, max(piles)
        best_speed = max_b

        while min_b <= max_b:
            mid = (min_b + max_b) // 2
            hours = 0
            for pile in piles:
                hours += int(pile / mid) + (pile % mid > 0)
            if hours <= h:
                best_speed = mid
                max_b = mid - 1
            else:
                min_b = mid + 1

        return best_speed