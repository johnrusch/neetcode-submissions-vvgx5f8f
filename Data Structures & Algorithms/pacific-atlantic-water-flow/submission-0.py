class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac_reach, atl_reach = set(), set()

        def dfs(r, c, reachable, prev_height): 
            if r < 0 or r >= len(heights) or c < 0 or c >= len(heights[r]) or (r, c) in reachable or heights[r][c] < prev_height:
                # return early, basecase
                return

            reachable.add((r, c))

            dfs(r - 1, c, reachable, heights[r][c])
            dfs(r + 1, c, reachable, heights[r][c])
            dfs(r, c - 1, reachable, heights[r][c])
            dfs(r, c + 1, reachable, heights[r][c])

        for i in range(len(heights[0])):
            dfs(0, i, pac_reach, heights[0][i])
            dfs(len(heights) - 1, i, atl_reach, heights[len(heights) - 1][i])

        for i in range(len(heights)):
            dfs(i, 0, pac_reach, heights[i][0])
            dfs(i, len(heights[i]) - 1, atl_reach, heights[i][len(heights[i]) - 1])

        # get the common cells between the sets

        return [[r, c] for r, c in pac_reach & atl_reach]