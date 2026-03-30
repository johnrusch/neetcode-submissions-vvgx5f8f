class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, h = 0, 1
        maxP = 0

        while h < len(prices):
            if prices[l] < prices[h]:
                currP = prices[h] - prices[l]
                maxP = max(maxP, currP)
            else:
                l = h
            h += 1

        return maxP