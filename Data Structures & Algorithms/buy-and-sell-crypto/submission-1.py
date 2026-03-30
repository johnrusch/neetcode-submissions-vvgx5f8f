class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return -1

        max_p = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[l] < prices[r]:
                curr_p = prices[r] - prices[l]
                max_p = max(max_p, curr_p)
            else:
                l = r
            r += 1

        return max_p

