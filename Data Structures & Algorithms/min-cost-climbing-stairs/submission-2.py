class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # add last step to cost array representing goal step
        # iterate backwards through array starting at 3rd from the end
        # at each cost, add the minimum cost from the two steps you can get to
        # (i + 1, i + 2)
        # once done iterating, first two indexes will have been updated
        # with costs to get through whole array, return the min

        cost.append(0)
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])