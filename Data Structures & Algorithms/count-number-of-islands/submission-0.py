class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # essentially just to mark the island we've found
        def explore(r, c):
            if grid[r][c] == "1":
                grid[r][c] = "#"
                if r > 0:
                    explore(r - 1, c)
                if c > 0:
                    explore(r, c - 1)
                if r < len(grid) - 1:
                    explore(r + 1, c)
                if c < len(grid[r]) - 1:
                    explore(r, c + 1)

        islands = 0
        # iterate through grid
        for i, row in enumerate(grid):
            for j, spot in enumerate(row):
                # when land found, explore land changing to "#"
                if spot == "1":
                    explore(i, j)
                    islands += 1

        return islands