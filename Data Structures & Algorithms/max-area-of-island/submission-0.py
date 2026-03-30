class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def explore(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[r]):
                return 0
            if grid[r][c] != 1:
                return 0

            grid[r][c] = "#"
            left = explore(r - 1, c)
            right = explore(r + 1, c)
            up = explore(r, c - 1)
            down = explore(r, c + 1)
            return left + right + up + down + 1

        max_area = 0
        # iterate through each square of the grid
        for i, row in enumerate(grid):
            for j, spot in enumerate(row):
                if spot == 1:
                    current = explore(i, j)
                    max_area = max(max_area, current)

        return max_area