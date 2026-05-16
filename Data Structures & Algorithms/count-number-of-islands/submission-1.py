class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        def explore(row, col):
            if grid[row][col] != "1":
                return

            grid[row][col] = "#"
            if row > 0:
                explore(row - 1, col)
            if row < len(grid) - 1:
                explore(row + 1, col)
            if col > 0:
                explore(row, col - 1)
            if col < len(grid[row]) - 1:
                explore(row, col + 1)


        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1":
                    res += 1
                    explore(r, c)

        return res