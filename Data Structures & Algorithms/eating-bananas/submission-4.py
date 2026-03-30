class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_b, max_b = 1, max(piles)
        res = max_b

        while min_b <= max_b:
            mid = (max_b + min_b) // 2
            hours = 0

            for pile in piles:
                hours += int(pile / mid) + (pile % mid > 0)

            if hours <= h:
                res = mid
                max_b = mid - 1
            else:
                min_b = mid + 1

        return res