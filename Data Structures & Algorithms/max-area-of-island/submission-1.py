class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def explore(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]):
                return 0
            if grid[row][col] != 1:
                return 0

            grid[row][col] = "#"
            up = explore(row - 1, col) 
            down = explore(row + 1, col) 
            left = explore(row, col - 1) 
            right = explore(row, col + 1) 
            return 1 + up + down + left + right

        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    island = explore(r, c)
                    res = max(res, island)

        return res